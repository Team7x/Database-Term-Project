-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 05, 2021 at 06:33 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ekspedisi`
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
('119140110', 'Aulia Rahman Zulfi', 'Jakarta', '2001-02-09');

-- --------------------------------------------------------

--
-- Table structure for table `kota`
--

CREATE TABLE `kota` (
  `id_kota` varchar(10) NOT NULL,
  `namaKota` varchar(50) NOT NULL,
  `hargaKota` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kota`
--

INSERT INTO `kota` (`id_kota`, `namaKota`, `hargaKota`) VALUES
('1', 'Jakarta', 15000),
('10', 'Makasar', 25000),
('2', 'Lampung', 17000),
('3', 'Palembang', 16000),
('4', 'Jambi', 18000),
('5', 'Banten', 16000),
('6', 'Bandung', 17000),
('7', 'Padang', 18000),
('8', 'Sorong', 30000),
('9', 'Bali', 20000);

-- --------------------------------------------------------

--
-- Table structure for table `kurir`
--

CREATE TABLE `kurir` (
  `nip` varchar(10) NOT NULL,
  `namaKurir` varchar(50) NOT NULL,
  `tgl_masuk` date NOT NULL,
  `alamatKurir` varchar(50) NOT NULL,
  `no_telp_Kurir` varchar(50) NOT NULL,
  `lamaKerja` date NOT NULL,
  `id_tipe` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kurir`
--

INSERT INTO `kurir` (`nip`, `namaKurir`, `tgl_masuk`, `alamatKurir`, `no_telp_Kurir`, `lamaKerja`, `id_tipe`) VALUES
('1', 'Bambang', '2015-09-01', 'Depok', '081234563532', '2019-10-06', '1');

-- --------------------------------------------------------

--
-- Table structure for table `order2`
--

CREATE TABLE `order2` (
  `resi` varchar(20) NOT NULL,
  `namaPengirim` varchar(50) NOT NULL,
  `namaPenerima` varchar(50) NOT NULL,
  `no_telp_pengirim` varchar(50) NOT NULL,
  `no_telp_penerima` varchar(50) NOT NULL,
  `alamat_penerima` varchar(50) NOT NULL,
  `beratBarang` int(10) NOT NULL,
  `tgl_pengiriman` date NOT NULL,
  `hargaTotal` int(10) NOT NULL,
  `nip` varchar(10) NOT NULL,
  `id_kota` varchar(10) NOT NULL,
  `id_status` varchar(10) NOT NULL,
  `estimasi` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order2`
--

INSERT INTO `order2` (`resi`, `namaPengirim`, `namaPenerima`, `no_telp_pengirim`, `no_telp_penerima`, `alamat_penerima`, `beratBarang`, `tgl_pengiriman`, `hargaTotal`, `nip`, `id_kota`, `id_status`, `estimasi`) VALUES
('143425243', 'Supriyadi', 'Paijo', '083424523243', '084324234141', 'Jakarta', 15, '2021-05-05', 15000, '1', '1', '0', '2021-05-06');

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `id_status` varchar(10) NOT NULL,
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
  `id_tipe` varchar(10) NOT NULL,
  `namaTipe` varchar(50) NOT NULL,
  `hargaTipe` int(5) NOT NULL,
  `lama` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tipe`
--

INSERT INTO `tipe` (`id_tipe`, `namaTipe`, `hargaTipe`, `lama`) VALUES
('1', 'REG', 9000, 3),
('2', 'FLASH', 17000, 1),
('3', 'INSTANT', 45000, 0);

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
