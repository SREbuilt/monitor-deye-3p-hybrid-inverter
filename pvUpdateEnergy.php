<?php

$cred = explode( "\n", file_get_contents( realpath(dirname(__FILE__)) . '/db.cred' ) );

$mysqli = new mysqli( $cred[0], $cred[1], $cred[2], $cred[3] );
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: " . $mysqli->connect_error;
} else {
	$sql = 
	"INSERT INTO `pv_E` ( `id`, `date`, `pv`, `grid_out`, `grid_in`, `battery_charge`, `battery_discharge`, `load`, `gen`)
		SELECT * FROM (SELECT
			NULL AS `id`,
			DATE(`timestamp`) AS `date`,
			(MAX(`pv_total_E`)-MIN(`pv_total_E`)) AS `pv`,
			(MAX(`grid_out_total_E`)-MIN(`grid_out_total_E`)) AS `grid_out`,
			(MAX(`grid_in_total_E`)-MIN(`grid_in_total_E`)) AS `grid_in`,
			(MAX(`battery_charge_total_E`)-MIN(`battery_charge_total_E`)) AS `battery_charge`,
			(MAX(`battery_discharge_total_E`)-MIN(`battery_discharge_total_E`)) AS `battery_discharge`,
			(MAX(`load_total_E`)-MIN(`load_total_E`)) AS `load`,
			(MAX(`gen_total_E`)-MIN(`gen_total_E`)) AS `gen`
		FROM
			`log`.`pv`
		WHERE
			DATE(`timestamp`) >= subdate(CURDATE(),1)
		GROUP BY
			DATE(`timestamp`)) AS `t`
	ON DUPLICATE KEY UPDATE `pv` = `t`.`pv`,`grid_out` = `t`.`grid_out`,`grid_in` = `t`.`grid_in`,`battery_charge` = `t`.`battery_charge`,`battery_discharge` = `t`.`battery_discharge`,`load` = `t`.`load`,`gen` = `t`.`gen`";
	$res = $mysqli->query( $sql );
}
