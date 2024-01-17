-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 17, 2024 at 04:59 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `listrik_pln`
--

-- --------------------------------------------------------

--
-- Table structure for table `pelanggan`
--

CREATE TABLE `pelanggan` (
  `id` int(11) NOT NULL,
  `nama_pelanggan` varchar(75) NOT NULL,
  `tarif_daya` varchar(30) NOT NULL,
  `tarif_watt` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pelanggan`
--

INSERT INTO `pelanggan` (`id`, `nama_pelanggan`, `tarif_daya`, `tarif_watt`) VALUES
(1111, 'Ida Anggraeni', 'R1M/900VA', 1500),
(1112, 'Mujiono', 'R1S/900VA', 750),
(1113, 'Suradi', 'R2M/1200VA', 2000);

-- --------------------------------------------------------

--
-- Table structure for table `tagihan`
--

CREATE TABLE `tagihan` (
  `resi` int(11) NOT NULL,
  `pelanggan_id` int(11) NOT NULL,
  `tanggal_bayar` date NOT NULL,
  `beban_penggunaan` int(11) NOT NULL,
  `tagihan` int(11) NOT NULL,
  `bulan_tahun` char(10) NOT NULL,
  `status` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tagihan`
--

INSERT INTO `tagihan` (`resi`, `pelanggan_id`, `tanggal_bayar`, `beban_penggunaan`, `tagihan`, `bulan_tahun`, `status`) VALUES
(1, 1111, '2024-01-17', 120, 180000, 'JAN/2024', 1),
(2, 1112, '2024-01-18', 100, 75000, 'JAN/2024', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pelanggan`
--
ALTER TABLE `pelanggan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tagihan`
--
ALTER TABLE `tagihan`
  ADD PRIMARY KEY (`resi`),
  ADD KEY `fk_tagihan` (`pelanggan_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pelanggan`
--
ALTER TABLE `pelanggan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1114;

--
-- AUTO_INCREMENT for table `tagihan`
--
ALTER TABLE `tagihan`
  MODIFY `resi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tagihan`
--
ALTER TABLE `tagihan`
  ADD CONSTRAINT `fk_tagihan` FOREIGN KEY (`pelanggan_id`) REFERENCES `pelanggan` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
