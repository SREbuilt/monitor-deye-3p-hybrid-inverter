-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 13, 2023 at 10:27 PM
-- Server version: 8.0.32-0ubuntu0.22.04.2
-- PHP Version: 8.1.2-1ubuntu2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `log`
--

-- --------------------------------------------------------

--
-- Table structure for table `pv`
--

CREATE TABLE `pv` (
  `row` int UNSIGNED NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `carport_P` smallint DEFAULT NULL,
  `carport_V` smallint DEFAULT NULL,
  `carport_I` smallint DEFAULT NULL,
  `roof_P` smallint DEFAULT NULL,
  `roof_V` smallint DEFAULT NULL,
  `roof_I` smallint DEFAULT NULL,
  `gen_p1_P` smallint DEFAULT NULL,
  `gen_p2_P` smallint DEFAULT NULL,
  `gen_p3_P` smallint DEFAULT NULL,
  `gen_P` smallint DEFAULT NULL,
  `DC_transformer_T` smallint DEFAULT NULL,
  `heatsink_T` smallint DEFAULT NULL,
  `battery_T` smallint DEFAULT NULL,
  `battery_V` smallint DEFAULT NULL,
  `battery_SOC` smallint DEFAULT NULL,
  `battery_P` smallint DEFAULT NULL,
  `battery_I` smallint DEFAULT NULL,
  `grid_P` smallint DEFAULT NULL,
  `load_total_P` smallint DEFAULT NULL,
  `backup_P` smallint DEFAULT NULL,
  `inverter_p1_V` smallint UNSIGNED DEFAULT NULL,
  `inverter_p2_V` smallint UNSIGNED DEFAULT NULL,
  `inverter_p3_V` smallint UNSIGNED DEFAULT NULL,
  `inverter_p1_P` smallint DEFAULT NULL,
  `inverter_p2_P` smallint DEFAULT NULL,
  `inverter_p3_P` smallint DEFAULT NULL,
  `inverter_P` smallint DEFAULT NULL,
  `inverter_frq` smallint UNSIGNED DEFAULT NULL,
  `load_frq` smallint UNSIGNED DEFAULT NULL,
  `grid_frq` smallint DEFAULT NULL,
  `battery_charge_today_E` smallint UNSIGNED DEFAULT NULL,
  `battery_discharge_today_E` smallint UNSIGNED DEFAULT NULL,
  `battery_charge_total_E` int UNSIGNED DEFAULT NULL,
  `battery_discharge_total_E` int UNSIGNED DEFAULT NULL,
  `grid_in_today_E` smallint UNSIGNED DEFAULT NULL,
  `grid_out_today_E` smallint UNSIGNED DEFAULT NULL,
  `grid_in_total_E` int UNSIGNED DEFAULT NULL,
  `grid_out_total_E` int UNSIGNED DEFAULT NULL,
  `load_today_E` smallint UNSIGNED DEFAULT NULL,
  `load_total_E` int UNSIGNED DEFAULT NULL,
  `pv_today_E` smallint UNSIGNED DEFAULT NULL,
  `pv_total_E` int UNSIGNED DEFAULT NULL,
  `gen_today_E` smallint UNSIGNED DEFAULT NULL,
  `gen_total_E` int UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `pv_E`
--

CREATE TABLE `pv_E` (
  `id` int UNSIGNED NOT NULL,
  `date` date NOT NULL,
  `pv` int UNSIGNED NOT NULL,
  `grid_out` int UNSIGNED NOT NULL,
  `grid_in` int UNSIGNED NOT NULL,
  `battery_charge` int UNSIGNED NOT NULL,
  `battery_discharge` int UNSIGNED NOT NULL,
  `load` int UNSIGNED NOT NULL,
  `gen` int UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `pv_values`
--

CREATE TABLE `pv_values` (
  `inverter_timestamp` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pv`
--
ALTER TABLE `pv`
  ADD PRIMARY KEY (`row`),
  ADD KEY `timestamp` (`timestamp`);

--
-- Indexes for table `pv_E`
--
ALTER TABLE `pv_E`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `date` (`date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pv`
--
ALTER TABLE `pv`
  MODIFY `row` int UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pv_E`
--
ALTER TABLE `pv_E`
  MODIFY `id` int UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;
