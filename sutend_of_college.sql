-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 20, 2021 at 06:27 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aswin`
--

-- --------------------------------------------------------

--
-- Table structure for table `sutend_of_college`
--

CREATE TABLE `sutend_of_college` (
  `id` int(11) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `Department` varchar(15) NOT NULL,
  `College` varchar(25) NOT NULL,
  `Mark_1` int(11) NOT NULL,
  `Mark_2` int(11) NOT NULL,
  `Mark_3` int(11) NOT NULL,
  `Mark_4` int(11) NOT NULL,
  `Mark_5` int(11) NOT NULL,
  `Total_Mark` int(11) NOT NULL,
  `Average` int(11) NOT NULL,
  `Grade` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sutend_of_college`
--

INSERT INTO `sutend_of_college` (`id`, `Name`, `Department`, `College`, `Mark_1`, `Mark_2`, `Mark_3`, `Mark_4`, `Mark_5`, `Total_Mark`, `Average`, `Grade`) VALUES
(2, 'Hareeni', 'ECE', 'Rajeshwari_Engineering', 90, 90, 78, 67, 90, 410, 89, 'A'),
(3, 'Rhaksha', 'CSE', 'Jeapier_Engineering', 86, 97, 71, 62, 93, 500, 90, 'A'),
(4, 'Aswinjoseph', 'MCT', 'Chennai_Institute_of_Tech', 99, 98, 78, 90, 99, 464, 93, 'S'),
(7, 'Saipriya', 'B.com', 'Jain_College', 90, 78, 67, 55, 69, 359, 72, 'A');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sutend_of_college`
--
ALTER TABLE `sutend_of_college`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sutend_of_college`
--
ALTER TABLE `sutend_of_college`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
