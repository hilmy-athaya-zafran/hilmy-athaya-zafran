-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 17, 2024 at 06:02 AM
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
-- Database: `dbpersediaan`
--

-- --------------------------------------------------------

--
-- Table structure for table `tblbarang`
--

CREATE TABLE `tblbarang` (
  `kd_barang` int(11) NOT NULL,
  `nm_barang` varchar(50) NOT NULL,
  `satuan` varchar(12) NOT NULL,
  `harga` int(11) NOT NULL,
  `stok` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tblbarang`
--

INSERT INTO `tblbarang` (`kd_barang`, `nm_barang`, `satuan`, `harga`, `stok`) VALUES
(1, 'roller', 'lusin', 9000, 26),
(2, 'per', 'lusin', 9000, 26);

-- --------------------------------------------------------

--
-- Table structure for table `tblbeli`
--

CREATE TABLE `tblbeli` (
  `nofak` varchar(5) NOT NULL,
  `tanggal` date NOT NULL,
  `kodesup` varchar(6) NOT NULL,
  `totalitem` int(11) NOT NULL,
  `totalbayar` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tblbeli`
--

INSERT INTO `tblbeli` (`nofak`, `tanggal`, `kodesup`, `totalitem`, `totalbayar`) VALUES
('2', '0000-00-00', '2', 2, 4),
('1', '0000-00-00', '1', 1, 1),
('3', '0000-00-00', '2', 0, 0),
('22', '2022-12-12', '1', 2, 800);

-- --------------------------------------------------------

--
-- Table structure for table `tbldetailbeli`
--

CREATE TABLE `tbldetailbeli` (
  `nofak` varchar(5) NOT NULL,
  `kd_barang` varchar(10) NOT NULL,
  `jml` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbldetailbeli`
--

INSERT INTO `tbldetailbeli` (`nofak`, `kd_barang`, `jml`) VALUES
('1', '1', 1),
('1', '2', 2),
('1', '1', 2),
('1', '2', 2),
('2', '2', 2),
('1', '1', 1),
('22', '1', 2);

-- --------------------------------------------------------

--
-- Table structure for table `tblsuplier`
--

CREATE TABLE `tblsuplier` (
  `kodesup` varchar(10) NOT NULL,
  `namasup` varchar(30) NOT NULL,
  `alamat` varchar(30) NOT NULL,
  `telp` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tblsuplier`
--

INSERT INTO `tblsuplier` (`kodesup`, `namasup`, `alamat`, `telp`) VALUES
('1', 'imi', 'padasuka', 8224001),
('2', 'hilmy', 'cimahi', 123123);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tblbarang`
--
ALTER TABLE `tblbarang`
  ADD PRIMARY KEY (`kd_barang`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tblbarang`
--
ALTER TABLE `tblbarang`
  MODIFY `kd_barang` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
