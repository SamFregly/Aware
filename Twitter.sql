-- phpMyAdmin SQL Dump
-- version 4.5.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 09, 2016 at 04:48 PM
-- Server version: 10.1.9-MariaDB
-- PHP Version: 7.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Twitter`
--

-- --------------------------------------------------------

--
-- Table structure for table `my_chart_data`
--

CREATE TABLE `my_chart_data` (
  `date` date NOT NULL,
  `pollRep` int(11) NOT NULL,
  `pollDem` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `my_chart_data`
--

INSERT INTO `my_chart_data` (`date`, `pollRep`, `pollDem`) VALUES
('2016-04-05', 28, 42),
('2016-04-07', 30, 45),
('2016-04-08', 28, 48),
('2016-04-10', 31, 46),
('2016-04-11', 30, 44),
('2016-04-13', 28, 41),
('2016-04-15', 31, 49),
('2016-04-17', 31, 45),
('2016-04-18', 33, 44),
('2016-04-21', 30, 42);

-- --------------------------------------------------------

--
-- Table structure for table `TBL_Account`
--

CREATE TABLE `TBL_Account` (
  `uid` int(11) NOT NULL,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `TBL_Account`
--

INSERT INTO `TBL_Account` (`uid`, `username`, `password`, `email`) VALUES
(1, 'wahidhadi24', '07221994w', 'wahidhadi24@gmail.com'),
(2, 'wahidhadi11', '07221994', 'wahidhadi24@gmail.com'),
(3, 'admin', '07221994', 'wahidhadi24@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `TBL_Case`
--

CREATE TABLE `TBL_Case` (
  `caseID` int(11) NOT NULL,
  `title` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `uid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `TBL_Case`
--

INSERT INTO `TBL_Case` (`caseID`, `title`, `description`, `uid`) VALUES
(1, 'Bernie Sanders', 'Bernie Dem Nom', 1),
(2, 'Hillary Clinton', 'Hillary Dem Nom', 2),
(3, 'Donal Trump', 'Trump GOP Nom', 2),
(4, 'Ted Cruz', 'Cruz GOP Nom', 1),
(6, 'Donald Trump', 'Trump GOP Nomination', 3),
(7, 'Kashich', 'Kasihgas', 3);

-- --------------------------------------------------------

--
-- Table structure for table `TBL_caseData`
--

CREATE TABLE `TBL_caseData` (
  `caseDataID` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  `value` float DEFAULT NULL,
  `caseID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `TBL_caseData`
--

INSERT INTO `TBL_caseData` (`caseDataID`, `date`, `value`, `caseID`) VALUES
(1, '2016-03-25', 44, 1),
(2, '2016-03-28', 50, 1),
(3, '2016-03-29', 45, 1),
(4, '2016-04-03', 55, 1),
(5, '2016-04-01', 48, 1),
(15, '2016-03-28', 33, 3),
(16, '2016-03-28', 40, 2),
(17, '2016-03-28', 26, 4),
(19, '2016-03-29', 36, 4),
(20, '2016-04-10', 55, 6),
(21, '2016-01-28', 25, 7),
(22, '2016-01-25', 30, 7);

-- --------------------------------------------------------

--
-- Table structure for table `TBL_Model`
--

CREATE TABLE `TBL_Model` (
  `model_ID` int(11) NOT NULL,
  `caseID` int(11) DEFAULT NULL,
  `path` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `TBL_Prediction`
--

CREATE TABLE `TBL_Prediction` (
  `prediction_ID` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  `value` int(11) DEFAULT NULL,
  `caseID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `TBL_Prediction`
--

INSERT INTO `TBL_Prediction` (`prediction_ID`, `date`, `value`, `caseID`) VALUES
(1, '2016-04-01', 34, 1),
(2, '2016-04-03', 45, 2),
(3, '2016-04-04', 32, 1),
(4, '2016-04-01', 33, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `TBL_Account`
--
ALTER TABLE `TBL_Account`
  ADD PRIMARY KEY (`uid`);

--
-- Indexes for table `TBL_Case`
--
ALTER TABLE `TBL_Case`
  ADD PRIMARY KEY (`caseID`),
  ADD KEY `uid` (`uid`);

--
-- Indexes for table `TBL_caseData`
--
ALTER TABLE `TBL_caseData`
  ADD PRIMARY KEY (`caseDataID`),
  ADD KEY `caseID` (`caseID`);

--
-- Indexes for table `TBL_Model`
--
ALTER TABLE `TBL_Model`
  ADD PRIMARY KEY (`model_ID`),
  ADD KEY `caseID` (`caseID`);

--
-- Indexes for table `TBL_Prediction`
--
ALTER TABLE `TBL_Prediction`
  ADD PRIMARY KEY (`prediction_ID`),
  ADD KEY `caseID` (`caseID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `TBL_Account`
--
ALTER TABLE `TBL_Account`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `TBL_Case`
--
ALTER TABLE `TBL_Case`
  MODIFY `caseID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `TBL_caseData`
--
ALTER TABLE `TBL_caseData`
  MODIFY `caseDataID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
--
-- AUTO_INCREMENT for table `TBL_Prediction`
--
ALTER TABLE `TBL_Prediction`
  MODIFY `prediction_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `TBL_Model`
--
ALTER TABLE `TBL_Model`
  ADD CONSTRAINT `tbl_model_ibfk_1` FOREIGN KEY (`caseID`) REFERENCES `TBL_Case` (`caseID`);

--
-- Constraints for table `TBL_Prediction`
--
ALTER TABLE `TBL_Prediction`
  ADD CONSTRAINT `prediction_case_fk` FOREIGN KEY (`prediction_ID`) REFERENCES `TBL_Case` (`caseID`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
