#!/usr/bin/env python
import minimalmodbus
import time
import struct
import sys
import mysql.connector
import deye
from pathlib import Path

p = Path(__file__).with_name('db.cred')
f = open(p.absolute(), 'r')
cred = f.read().splitlines()

mydb = mysql.connector.connect(
  host=cred[0],
  user=cred[1],
  password=cred[2],
  database=cred[3]
)

mycursor = mydb.cursor()

sql_fields = []
sql_values = []
for register in deye.registers:
	if ( register[deye.reg_log] == 1 ):
		sql_fields.append( ' `' + register[deye.reg_db_field] + '`' )
		sql_values.append( ' %s' )

sqlInsertData = 'INSERT INTO `pv` ( `timestamp`,{fields} ) VALUES ( NOW(),{values} )'.format(
		fields=",".join(sql_fields),
		values=",".join(sql_values)
	)

# get last data timestamp
mycursor.execute("SELECT UNIX_TIMESTAMP(`timestamp`) FROM `pv` ORDER BY `timestamp` DESC LIMIT 1")
myresult = mycursor.fetchall()
for x in myresult:
	lastLogTimestamp = x[0]

#sys.exit()

# port name, slave address (in decimal)
inverter = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
inverter.serial.baudrate = 9600
inverter.serial.bytesize = 8
inverter.serial.parity   = minimalmodbus.serial.PARITY_NONE
inverter.serial.stopbits = 1
inverter.mode = minimalmodbus.MODE_RTU
inverter.serial.timeout  = 1
inverter.close_port_after_each_call = True
#inverter.debug = True
#print(inverter)

startTime = time.time()
# avg over samples
samples = 0
errors = 0
while True:
	start = 500
	d = 100
	#if ( len(sys.argv) > 1 ):
	#	start = int(sys.argv[1])

	try:
		while start < 601:
			# Start register, number, function code
			data = inverter.read_registers(start, d, 3)
			#print(data)
			n = len(data)
			for i in range(0,n):
				j = i + start
				if ( j in deye.ref_registers ):
					r = deye.ref_registers[j]
					if ( r[deye.reg_type] == 's16' ):
						r[deye.reg_value] += data[i] - ((data[i] & 0x8000) << 1)
					elif ( r[deye.reg_type] == 'v16' ):
						if ( data[i] != 42991 ):
							r[deye.reg_value] += data[i]
					else:
						r[deye.reg_value] += data[i]
					# add high word onto lower
					if ( r[deye.reg_log] == 2 ):
						lr = deye.ref_registers[r[deye.reg_db_field]]
						lr[deye.reg_value] += r[deye.reg_scale] * (r[deye.reg_value] + r[deye.reg_offset])

			start += d
		samples += 1

		# log to db
		now = time.time()
		if ( now - startTime > 9.5 ):
			#log null row
			if ( now - lastLogTimestamp > 30 ):
				val = []
				val.append( round( (now + lastLogTimestamp) / 2 ) )
				mycursor.execute("INSERT INTO `pv` ( `timestamp` ) VALUES ( FROM_UNIXTIME(%s) )", val)
				mydb.commit()
			
			#toggle gen port
			gen = inverter.read_registers(133, 1, 3)
			if ( ( deye.ref_registers[672][deye.reg_value] / samples ) > 100 and ( deye.ref_registers[673][deye.reg_value] / samples ) > 100 ):
				if ( gen[0] != 2 ):
					inverter.write_register(133, 2, 0, 16, False)
			else:
				if ( gen[0] != 1 ):
					inverter.write_register(133, 1, 0, 16, False)

			#insert to db
			val = []
			for r in deye.registers:
				if ( r[deye.reg_log] == 1 ):
					val.append( round( r[deye.reg_value] / samples ) )
				r[deye.reg_value] = 0

			mycursor.execute(sqlInsertData, val)
			mydb.commit()

			lastLogTimestamp = now

			#get inverter datetime
			date = inverter.read_registers(62, 3, 3)
			year = (date[0] >> 8) + 2000
			month = date[0] & 255
			day = (date[1] >> 8)
			hour = date[1] & 255
			minute = (date[2] >> 8)
			second = date[2] & 255

			timeSql = 'UPDATE `pv_values` SET `inverter_timestamp` = "{year}-{month}-{day} {hour}:{minute}:{second}"'.format( year = year, month = month, day = day, hour = hour, minute = minute, second = second)
			mycursor.execute(timeSql)
			mydb.commit()


			samples = 0
			errors = 0
			startTime = time.time()
	except Exception as error:
		#print( "[!] Exception occurred: ", error )
		errors += 1
		if ( errors > 100 ):
			print("getInverterDeye: exit, too many errors")
			sys.exit()
		time.sleep(2)

	time.sleep(1)