-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: sql6.freesqldatabase.com
-- Generation Time: May 09, 2021 at 11:56 AM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sql6410548`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `nim` varchar(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`nim`, `name`, `alamat`, `password`) VALUES
('1', '1', '1', '1'),
('119140110', 'Aulia Rahman Zulfi', 'Jakarta', '2001-02-09'),
('119140190', 'Sayyid Muhammad Umar Al Haris', 'Jalan Demang Lebar Daun Palembang', '2001-10-12');

-- --------------------------------------------------------

--
-- Table structure for table `kota`
--

CREATE TABLE `kota` (
  `id_kota` int(10) NOT NULL,
  `namaKota` varchar(50) NOT NULL,
  `hargaKota` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `kurir`
--

CREATE TABLE `kurir` (
  `nip` int(10) NOT NULL,
  `namaKurir` varchar(50) NOT NULL,
  `tgl_masuk` date NOT NULL,
  `alamatKurir` varchar(50) NOT NULL,
  `no_telp_Kurir` varchar(50) NOT NULL,
  `id_tipe` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `order2`
--

CREATE TABLE `order2` (
  `resi` int(20) NOT NULL,
  `namaPengirim` varchar(50) NOT NULL,
  `namaPenerima` varchar(50) NOT NULL,
  `no_telp_pengirim` varchar(50) NOT NULL,
  `no_telp_penerima` varchar(50) NOT NULL,
  `alamat_penerima` varchar(50) NOT NULL,
  `beratBarang` int(10) NOT NULL,
  `tgl_pengiriman` date NOT NULL,
  `hargaTotal` int(10) NOT NULL,
  `nip` int(10) NOT NULL,
  `id_kota` int(10) NOT NULL,
  `id_status` int(10) NOT NULL,
  `estimasi` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `id_status` int(10) NOT NULL,
  `namaStatus` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `status`
--

INSERT INTO `status` (`id_status`, `namaStatus`) VALUES
('0', 'On Process'),
('1', 'Delivered');

-- --------------------------------------------------------

--
-- Table structure for table `tipe`
--

CREATE TABLE `tipe` (
  `id_tipe` int(10) NOT NULL,
  `namaTipe` varchar(50) NOT NULL,
  `hargaTipe` int(5) NOT NULL,
  `lama` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tipe`
--

INSERT INTO `tipe` (`id_tipe`, `namaTipe`, `hargaTipe`, `lama`) VALUES
('1', 'REG', 2, 5),
('2', 'FLASH', 3, 3),
('3', 'INSTANT', 4, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`nim`);

--
-- Indexes for table `kota`
--
ALTER TABLE `kota`
  ADD PRIMARY KEY (`id_kota`);

--
-- Indexes for table `kurir`
--
ALTER TABLE `kurir`
  ADD PRIMARY KEY (`nip`),
  ADD KEY `id_tipe` (`id_tipe`);

--
-- Indexes for table `order2`
--
ALTER TABLE `order2`
  ADD PRIMARY KEY (`resi`),
  ADD KEY `nip` (`nip`),
  ADD KEY `id_kota` (`id_kota`),
  ADD KEY `id_status` (`id_status`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`id_status`);

--
-- Indexes for table `tipe`
--
ALTER TABLE `tipe`
  ADD PRIMARY KEY (`id_tipe`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `kurir`
--
ALTER TABLE `kurir`
  ADD CONSTRAINT `kurir_ibfk_1` FOREIGN KEY (`id_tipe`) REFERENCES `tipe` (`id_tipe`);

--
-- Constraints for table `order2`
--
ALTER TABLE `order2`
  ADD CONSTRAINT `order2_ibfk_1` FOREIGN KEY (`nip`) REFERENCES `kurir` (`nip`),
  ADD CONSTRAINT `order2_ibfk_2` FOREIGN KEY (`id_kota`) REFERENCES `kota` (`id_kota`),
  ADD CONSTRAINT `order2_ibfk_3` FOREIGN KEY (`id_status`) REFERENCES `status` (`id_status`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
