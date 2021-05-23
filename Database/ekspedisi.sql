-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: sql6.freesqldatabase.com
-- Generation Time: May 23, 2021 at 10:26 AM
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
-- Database: `sql6413208`
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

--
-- Dumping data for table `kota`
--

INSERT INTO `kota` (`id_kota`, `namaKota`, `hargaKota`) VALUES
(1, 'Palembang', 16000),
(2, 'Jakarta', 13000),
(3, 'Bali', 20000),
(4, 'Bandung', 14000),
(5, 'Manado', 35000),
(6, 'New Delhi', 139000);

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

--
-- Dumping data for table `kurir`
--

INSERT INTO `kurir` (`nip`, `namaKurir`, `tgl_masuk`, `alamatKurir`, `no_telp_Kurir`, `id_tipe`) VALUES
(1, 'Joni', '2021-01-13', 'Jalan Sepuncak', '081285671346', 1),
(2, 'Odin', '2011-03-16', 'Kemanggisan', '084435234342', 1),
(3, 'Dino', '2017-01-11', 'Cisalak', '084324321323', 2),
(4, 'Khloe', '2021-05-05', 'Bevery Hills', '081100001111', 2),
(5, 'Kurbar', '2021-05-18', 'Jalan Semanggis', '081234567890', 3);

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

--
-- Dumping data for table `order2`
--

INSERT INTO `order2` (`resi`, `namaPengirim`, `namaPenerima`, `no_telp_pengirim`, `no_telp_penerima`, `alamat_penerima`, `beratBarang`, `tgl_pengiriman`, `hargaTotal`, `nip`, `id_kota`, `id_status`, `estimasi`) VALUES
(543676575, 'Parjo', 'Deka', '085435343426', '085435345654', 'Jalan Denpasar', 8, '2021-05-19', 160000, 1, 3, 1, '2021-05-24'),
(543676576, 'Sayyid', 'Haris', '08953485023', '081231827122', 'Jalan Sepuncak', 3, '2021-05-19', 96000, 5, 1, 1, '2021-05-20'),
(543676577, 'Sims', 'Maung', '08123126382', '08187236182', 'Jalan Cambuk Kemayoran', 4, '2021-05-19', 52000, 2, 2, 0, '2021-05-24'),
(543676578, 'Auau', 'Padil', '085346577564', '082178696789', 'Jalan Spens Bersatu', 11, '2021-05-19', 176000, 1, 1, 0, '2021-05-24'),
(543676579, 'Kaith', 'Ky', '081221122112', '082112211221', 'Tengkiyu Foreva Street', 1, '2021-05-19', 139000, 2, 6, 0, '2021-05-24');

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
(0, 'On Process'),
(1, 'Delivered');

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
(1, 'REG', 2, 5),
(2, 'FLASH', 3, 3),
(3, 'INSTANT', 4, 1);

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
