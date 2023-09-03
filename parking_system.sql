USE parking_system;
 
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `emplogin`;
CREATE TABLE IF NOT EXISTS `emplogin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(30) DEFAULT NULL,
  `pwd` char(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `adminlogin`;
CREATE TABLE IF NOT EXISTS `adminlogin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(30) DEFAULT NULL,
  `pwd` char(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
--
-- Dumping data for table `login`
--

INSERT INTO `emplogin` (`id`, `name`, `pwd`) VALUES
(1, 'Arpit', 'Sarap'),
(2, 'Jitesh', 'Sanap');

INSERT INTO `adminlogin` (`id`, `name`, `pwd`) VALUES
(1, 'Sumant', 'Reddy'),
(2, 'Talha', 'Shaikh');

select * from emplogin;
select * from adminlogin;

-- --------------------------------------------------------

--
-- Table structure for table `parking_space`
--

DROP TABLE IF EXISTS `parking_space`;
CREATE TABLE IF NOT EXISTS `parking_space` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_id` int(11) DEFAULT NULL,
  `status` char(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `parking_space`
--

INSERT INTO `parking_space` (`id`, `type_id`, `status`) VALUES
(1, 1, 'full'),
(2, 2, 'full'),
(3, 3, 'open'),
(4, 4, 'open'),
(5, 5, 'open'),
(6, 1, 'open'),
(7, 1, 'open'),
(8, 1, 'open'),
(9, 1, 'open'),
(10, 1, 'open'),
(11, 1, 'open'),
(12, 1, 'open'),
(13, 2, 'open'),
(14, 2, 'open'),
(15, 2, 'open'),
(16, 2, 'open'),
(17, 2, 'open'),
(18, 2, 'open'),
(19, 2, 'open'),
(20, 3, 'open'),
(21, 3, 'open'),
(22, 3, 'open'),
(23, 3, 'open'),
(24, 3, 'open'),
(25, 4, 'open'),
(26, 4, 'open'),
(27, 5, 'open'),
(28, 5, 'open'),
(29, 9, 'open'),
(30, 9, 'open');

-- --------------------------------------------------------

--
-- Table structure for table `parking_type`
--

DROP TABLE IF EXISTS `parking_type`;
CREATE TABLE IF NOT EXISTS `parking_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(20) DEFAULT NULL,
  `price` float(7,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `parking_type`
--

INSERT INTO `parking_type` (`id`, `name`, `price`) VALUES
(1, 'Two Wheelar', 30.00),
(2, 'car', 50.00),
(3, 'bus', 250.00),
(4, 'Truck', 350.00),
(5, 'trolly', 450.00),
(6, 'Cycle', 20.00),
(7, 'cycle', 20.00),
(8, 'motor cycle', 20.00),
(9, 'E-cycle', 35.00);

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
CREATE TABLE IF NOT EXISTS `transaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_id` char(20) DEFAULT NULL,
  `parking_id` int(11) DEFAULT NULL,
  `entry_date` date DEFAULT NULL,
  `entry_time` char(20) DEFAULT NULL,
  `exit_date` date DEFAULT NULL,
  `exit_time` char(20) DEFAULT NULL,
  `amount` float(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`id`, `vehicle_id`, `parking_id`, `entry_date`, `exit_date`, `amount`) VALUES
(1, 'mh24z-9498', 1, '2022-05-20', '2022-05-20', 30.00),
(2, 'mh21af-5158', 29, '2022-05-20', '2022-05-20', 35.00),
(3, 'mh12az-1090', 1, '2022-05-21', NULL, NULL),
(4, 'mh12bz-1011', 2, '2022-05-21', NULL, NULL);
COMMIT;

