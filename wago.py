reg_num = 0
reg_db_field = 1
reg_name = 2
reg_type = 3
reg_offset = 4
reg_scale = 5
reg_unit = 6
reg_log = 7
reg_value = 8

registers = (
	[ 0x5002,	'L1_V',						'L1 to N voltage',							'f32', 0, 1.00,	'V',	1, 0 ],
	[ 0x5004,	'L2_V',						'L2 to N voltage',							'f32', 0, 1.00,	'V',	1, 0 ],
	[ 0x5006,	'L3_V',						'L3 to N voltage',							'f32', 0, 1.00,	'V',	1, 0 ],
	[ 0x5008,	'frq',						'Grid frequency',							'f32', 0, 1.00,	'Hz',	1, 0 ],
	[ 0x500C,	'L1_C',						'L1 current',								'f32', 0, 1.00,	'A',	1, 0 ],
	[ 0x500E,	'L2_C',						'L2 current',								'f32', 0, 1.00,	'A',	1, 0 ],
	[ 0x5010,	'L3_C',						'L3 current',								'f32', 0, 1.00,	'A',	1, 0 ],
	[ 0x5012,	'P',						'Total power',								'f32', 0, 1.00,	'W',	1, 0 ],
	[ 0x5014,	'L1_P',						'L1 power',									'f32', 0, 1.00,	'W',	1, 0 ],
	[ 0x5016,	'L2_P',						'L2 power',									'f32', 0, 1.00,	'W',	1, 0 ],
	[ 0x5018,	'L3_P',						'L3 power',									'f32', 0, 1.00,	'W',	1, 0 ],
	[ 0x501A,	'RP',						'Total reactive power',						'f32', 0, 1.00,	'VAr',	1, 0 ],
	[ 0x501C,	'L1_RP',					'L1 reactive power',						'f32', 0, 1.00,	'VAr',	1, 0 ],
	[ 0x501E,	'L2_RP',					'L2 reactive power',						'f32', 0, 1.00,	'VAr',	1, 0 ],
	[ 0x5020,	'L3_RP',					'L3 reactive power',						'f32', 0, 1.00,	'VAr',	1, 0 ],
	[ 0x5022,	'AP',						'Total apparent power',						'f32', 0, 1.00,	'VA',	1, 0 ],
	[ 0x5024,	'L1_AP',					'L1 apparent power',						'f32', 0, 1.00,	'VA',	1, 0 ],
	[ 0x5026,	'L2_AP',					'L2 apparent power',						'f32', 0, 1.00,	'VA',	1, 0 ],
	[ 0x5028,	'L3_AP',					'L3 apparent power',						'f32', 0, 1.00,	'VA',	1, 0 ],
	[ 0x502A,	'PF',						'Total power factor',						'f32', 0, 1.00,	'',		1, 0 ],
	[ 0x502C,	'L1_PF',					'L1 power factor',							'f32', 0, 1.00,	'',		1, 0 ],
	[ 0x502E,	'L2_PF',					'L2 power factor',							'f32', 0, 1.00,	'',		1, 0 ],
	[ 0x5030,	'L3_PF',					'L3 power factor',							'f32', 0, 1.00,	'',		1, 0 ],
	[ 0x5032,	'L1_L2_V',					'L1 to L2 voltage',							'f32', 0, 1.00,	'V',	1, 0 ],
	[ 0x5034,	'L1_L3_V',					'L1 to L3 voltage',							'f32', 0, 1.00,	'V',	1, 0 ],
	[ 0x5036,	'L2_L3_V',					'L2 to L3 voltage',							'f32', 0, 1.00,	'V',	1, 0 ],
	[ 0x6000,	'E',						'Total energy',								'f32', 0, 1.00,	'kWh',	1, 0 ],
	[ 0x6002,	'T1_E',						'T1 Total energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x6004,	'T2_E',						'T2 Total energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x6006,	'L1_E',						'L1 Total energy',							'f32', 0, 1.00,	'kWh',	1, 0 ],
	[ 0x6008,	'L2_E',						'L2 Total energy',							'f32', 0, 1.00,	'kWh',	1, 0 ],
	[ 0x600A,	'L3_E',						'L3 Total energy',							'f32', 0, 1.00,	'kWh',	1, 0 ],
	[ 0x600C,	'import_E',					'Import energy',							'f32', 0, 1.00,	'kWh',	1, 0 ],
	[ 0x600E,	'import_T1_E',				'T1 Import energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x6010,	'import_T2_E',				'T2 Import energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x6012,	'import_L1_E',				'L1 Import energy',							'f32', 0, 1.00,	'kWh',	1, 0 ],
	[ 0x6014,	'import_L2_E',				'L2 Import energy',							'f32', 0, 1.00,	'kWh',	1, 0 ],
	[ 0x6016,	'import_L3_E',				'L3 Import energy',							'f32', 0, 1.00,	'kWh',	1, 0 ],
	[ 0x6018,	'export_E',					'Export energy',							'f32', 0, 1.00,	'kWh',	1, 0 ],
	[ 0x601A,	'export_T1_E',				'T1 Export energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x601C,	'export_T2_E',				'T2 Export energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x601E,	'export_L1_E',				'L1 Export energy',							'f32', 0, 1.00,	'kWh',	1, 0 ],
	[ 0x6020,	'export_L2_E',				'L2 Export energy',							'f32', 0, 1.00,	'kWh',	1, 0 ],
	[ 0x6022,	'export_L3_E',				'L3 Export energy',							'f32', 0, 1.00,	'kWh',	1, 0 ],
	[ 0x6024,	'RE',						'Total reactive energy',					'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6026,	'T1_RE',					'T1 Total reactive energy',					'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6028,	'T2_RE',					'T2 Total reactive energy',					'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x602A,	'L1_RE',					'L1 Total reactive energy',					'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x602C,	'L2_RE',					'L2 Total reactive energy',					'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x602E,	'L3_RE',					'L3 Total reactive energy',					'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6030,	'import_RE',				'Import reactive energy',					'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6032,	'import_T1_RE',				'T1 Import reactive energy',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6034,	'import_T2_RE',				'T2 Import reactive energy',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6036,	'import_L1_RE',				'L1 Import reactive energy',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6038,	'import_L2_RE',				'L2 Import reactive energy',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x603A,	'import_L3_RE',				'L3 Import reactive energy',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x603C,	'export_RE',				'Export reactive energy',					'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x603E,	'export_T1_RE',				'T1 Export reactive energy',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6040,	'export_T2_RE',				'T2 Export reactive energy',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6042,	'export_L1_RE',				'L1 Export reactive energy',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6044,	'export_L2_RE',				'L2 Export reactive energy',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6046,	'export_L3_RE',				'L3 Export reactive energy',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6048,	'tariff',					'Tariff',									's16', 0, 1.00,	'',		0, 0 ],
	[ 0x6049,	'',							'Trip energy',								'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x604B,	'T3_E',						'T3 Total energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x604D,	'T4_E',						'T4 Total energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x604F,	'import_T3_E',				'T3 Import energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x6051,	'import_T4_E',				'T4 Import energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x6053,	'export_T3_E',				'T3 Export energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x6055,	'export_T4_E',				'T4 Export energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x6057,	'T3_RE',					'T3 Total reactive energy',					'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6059,	'T4_RE',					'T4 Total reactive energy',					'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x605B,	'import_T3_RE',				'T3 Import reactive energy',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x605D,	'import_T4_RE',				'T4 Import reactive energy',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x605F,	'export_T3_RE',				'T3 Export reactive energy',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6061,	'export_T4_RE',				'T4 Export reactive energy',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6063,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6065,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6067,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6069,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x606B,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x606D,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x606F,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6071,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6073,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6075,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6077,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6079,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x607B,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x607D,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x607F,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6081,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6083,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6085,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6087,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x6089,	'',							'',				'f32', 0, 1.00,	'kVArh',0, 0 ],
	[ 0x608B,	'',							'L1 Trip energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x608D,	'',							'L2 Trip energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
	[ 0x608F,	'',							'L3 Trip energy',							'f32', 0, 1.00,	'kWh',	0, 0 ],
)

ref_registers = {}

for register in registers:
	ref_registers[ register[0] ] = register