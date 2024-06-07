-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 21, 2024 at 07:33 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `api_android`
--

-- --------------------------------------------------------

--
-- Table structure for table `control_manual`
--

CREATE TABLE `control_manual` (
  `id` int(255) NOT NULL,
  `userId` int(11) NOT NULL,
  `jenis_tank` varchar(255) NOT NULL,
  `jenis_hewan` varchar(255) NOT NULL,
  `buka_servo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `control_manual`
--

INSERT INTO `control_manual` (`id`, `userId`, `jenis_tank`, `jenis_hewan`, `buka_servo`) VALUES
(29, 0, 'Tabung 2', 'Kucing', 1),
(30, 0, 'Tabung 2', 'Kucing', 0),
(31, 0, 'Tabung 2', 'Kucing', 0),
(32, 0, 'Tabung 2', 'Kucing', 1),
(33, 0, 'Tabung 2', 'Kucing', 0),
(34, 0, 'Tabung 2', 'Kucing', 1),
(35, 0, 'Tabung 2', 'Kucing', 0),
(36, 5, '1', 'anjing', 1),
(37, 7, 'Tabung 1', 'Anjing', 1),
(38, 7, 'Tabung 1', 'Kucing', 1),
(39, 7, 'Tabung 1', 'Kucing', 1),
(40, 7, 'Tabung 2', 'Kucing', 1),
(41, 7, 'Tabung 1', 'Kucing', 1),
(42, 7, 'Tabung 1', 'Kucing', 0),
(43, 7, 'Tabung 1', 'Kucing', 0),
(44, 7, 'Tabung 1', 'Kucing', 1),
(45, 7, 'Tabung 1', 'Kucing', 0),
(46, 7, 'Tabung 1', 'Kucing', 1),
(47, 7, 'Tabung 1', 'Kucing', 0),
(48, 7, 'Tabung 2', 'Kucing', 1),
(49, 7, 'Tabung 2', 'Kucing', 0);

-- --------------------------------------------------------

--
-- Table structure for table `reguster`
--

CREATE TABLE `reguster` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reguster`
--

INSERT INTO `reguster` (`id`, `email`, `nama`, `username`, `password`) VALUES
(5, 'muhsyalbs@gmail.com', 'aksyal', 'aksyal', 'bambangsusano'),
(7, 'xboxandsteam@gmail.com', 'xboxaja', 'xboxsteam', 'xboxsteam0123');

-- --------------------------------------------------------

--
-- Table structure for table `schedule_alarm`
--

CREATE TABLE `schedule_alarm` (
  `id` int(11) NOT NULL,
  `userId` int(11) NOT NULL,
  `waktu` varchar(255) NOT NULL,
  `jns_hewan` varchar(255) NOT NULL,
  `jns_tank` varchar(255) NOT NULL,
  `jmlh_pakan` varchar(255) NOT NULL,
  `kondisi_switch` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `schedule_alarm`
--

INSERT INTO `schedule_alarm` (`id`, `userId`, `waktu`, `jns_hewan`, `jns_tank`, `jmlh_pakan`, `kondisi_switch`) VALUES
(3, 5, '13.00 AM', 'anjing', 'kedua', '35gr', 1),
(4, 5, '02:20 PM', 'anjing', '1', '35gr', 1),
(11, 5, '02:00 AM', 'anjing', '1', '35gr', 1),
(12, -1, '10:55 AM', 'kucing', '1', '1gr', 0),
(13, 7, '09:00 PM', 'anjing', '1', '1gp', 0),
(14, 5, '', '', '', '', 1),
(15, 7, '03:10 PM', 'anjing', '2', '120gr', 0),
(16, 7, '04:15 PM', 'kucing', '1', '50gr', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `control_manual`
--
ALTER TABLE `control_manual`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reguster`
--
ALTER TABLE `reguster`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `schedule_alarm`
--
ALTER TABLE `schedule_alarm`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `control_manual`
--
ALTER TABLE `control_manual`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `reguster`
--
ALTER TABLE `reguster`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `schedule_alarm`
--
ALTER TABLE `schedule_alarm`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
