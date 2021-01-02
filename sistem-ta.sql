-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2021 at 03:27 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sistem-ta`
--

-- --------------------------------------------------------

--
-- Table structure for table `dosen`
--

CREATE TABLE `dosen` (
  `id` int(11) NOT NULL,
  `username` varchar(32) NOT NULL,
  `password` varchar(100) NOT NULL,
  `name` varchar(128) NOT NULL,
  `email` varchar(64) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `nip` varchar(16) NOT NULL,
  `access` varchar(16) NOT NULL DEFAULT 'dosen',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dosen`
--

INSERT INTO `dosen` (`id`, `username`, `password`, `name`, `email`, `phone`, `nip`, `access`, `createdAt`, `updatedAt`) VALUES
(1, 'dosen', '$5$rounds=535000$vYFaOYLdVZqXcJEN$o8XmacmgliVzhzxgAxcMYntIepdqlkdv1O57eK/dbjD', 'tesataest', 'teat@gmail.com', '131313', '11', 'dosen', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(2, 'qqqqqqqqqqqqqw', '$5$rounds=535000$NQ5HhOcKnEEg10ut$0ctf1Ebk8cX/jTUb5y5MgjZSw/C9NfQl.o86/Flu4n.', 'dfff', 'aefaesgg@gmail.com', '33', '3333', 'dosen', '2021-01-02 21:18:28', '2021-01-02 21:18:28');

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `name` text,
  `nim` varchar(9) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `jurusan_id` int(3) DEFAULT NULL,
  `prodi_id` int(3) DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mahasiswa`
--

INSERT INTO `mahasiswa` (`id`, `username`, `password`, `name`, `nim`, `email`, `phone`, `jurusan_id`, `prodi_id`, `createdAt`, `updatedAt`) VALUES
(1, 'test', 'password', 'test', '181511025', 'test@gmail.com', '1212424213', 1, 2, '2020-12-30 00:00:00', '2020-12-30 00:00:00'),
(2, 'acikiwir1', '$5$rounds=535000$vYFaOYLdVZqXcJEN$o8XmacmgliVzhzxgAxcMYntIepdqlkdv1O57eK/dbjD', 'aaaddddd', '4124', 'saet@gmail.com', '1341414', 1, 1, '2021-01-01 14:38:24', '2021-01-01 14:38:24'),
(3, 'ilham', '$5$rounds=535000$DPbg59mfhDXb3/oO$KNvPujQCnNNY0HmWlz1vWIaTT0nTCeEpcacxlbumSv5', 'test', '181511012', 'testuser@gmail.com', '12121231', 1, 1, '2021-01-01 17:52:11', '2021-01-01 17:52:11'),
(4, 'mahasiswa', '$5$rounds=535000$7UJT9OH4chsBBohA$tKIqwU4bvwOLiSPd00pVy2gPTJHViuXntjfYLW.22C3', 'ini mahasiswa', '13513', 'siswa@gmail.com', '1241', 1, 1, '2021-01-02 18:35:41', '2021-01-02 18:35:41'),
(5, 'aku', '$5$rounds=535000$sBUg7gYf0uEZcM7n$GBRL8adeKtBH7Hzz7XKU5.vWR7PqibSKhIaDPGZjIeD', 'admin', '13131', 'admin@gmail.com', '1313', 3, 3, '2021-01-02 20:31:24', '2021-01-02 20:31:24'),
(6, 'aweaeae', '$5$rounds=535000$gIPjzV0AjO468bo3$F.LlAiGG/ylVCE7L36v3/Fi.QaNxX5AU1xi5vlIeQO9', 'tesat', '1111', 'as@gmail.com', '1212123', 1, 1, '2021-01-02 21:15:25', '2021-01-02 21:15:25');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dosen`
--
ALTER TABLE `dosen`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dosen`
--
ALTER TABLE `dosen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
