-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2024 at 12:56 AM
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
-- Database: `librarydatabase`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `book_ID` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `publisher` varchar(100) DEFAULT NULL,
  `publicationYear` int(11) DEFAULT NULL,
  `ddc` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`book_ID`, `title`, `author`, `publisher`, `publicationYear`, `ddc`) VALUES
(1, 'Pride and Prejudice', 'Jane Austen', 'N/A', 1813, 823),
(2, '1984', 'George Orwell', 'Secker and Warburg', 1949, 823),
(3, 'Crime and Punishment', 'Fyodor Dostoevsky', 'Penguin Classics', 1866, 742),
(4, 'Hamlet', 'William Shakespeare', 'N/A', 1623, 822),
(5, 'One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 'Editorial Sudamericana', 1967, 863),
(6, 'Anna Karenina', 'Leo Tolstoy', 'Macrae Smith Company', 1919, 891),
(7, 'The Oddysey', 'Homer', 'N/A', 1488, 883),
(8, 'The Stranger', 'Albert Camus', 'Vintage International', 1989, 843),
(9, 'The Brothers Karamazov', 'Fyodor Dostoevsky', 'Farrar, Straus and Giroux', 2002, 891),
(10, 'Great Expectations', 'Charles Dickens', 'Oxford University Press', 1998, 823);

-- --------------------------------------------------------

--
-- Table structure for table `borrowedbooks`
--

CREATE TABLE `borrowedbooks` (
  `book_ID` int(11) NOT NULL,
  `borrowID` int(11) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `publisher` varchar(100) DEFAULT NULL,
  `publicationYear` int(11) DEFAULT NULL,
  `ddc` int(11) DEFAULT NULL,
  `borrowDate` date DEFAULT NULL,
  `returnDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `borrowedbooks`
--

INSERT INTO `borrowedbooks` (`book_ID`, `borrowID`, `title`, `author`, `publisher`, `publicationYear`, `ddc`, `borrowDate`, `returnDate`) VALUES
(1, 4, 'Pride and Prejudice', 'Jane Austen', 'N/A', 1813, 823, '2024-12-07', '2024-12-09'),
(2, 7, '1984', 'George Orwell', 'Secker and Warburg', 1949, 823, '2024-12-12', '2024-12-15'),
(3, 5, 'Crime and Punishment', 'Fyodor Dostoevsky', 'Penguin Classics', 1866, 742, '2024-12-09', '2024-12-11'),
(4, 1, 'Hamlet', 'William Shakespeare', 'N/A', 1623, 822, '2024-12-02', '2024-12-04'),
(5, 6, 'One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 'Editorial Sudamericana', 1967, 863, '2024-12-02', '2024-12-05'),
(6, 10, 'Anna Karenina', 'Leo Tolstoy', 'Macrae Smith Company', 1919, 891, '2024-12-07', '2024-12-08'),
(7, 8, 'The Oddysey', 'Homer', 'N/A', 1488, 883, '2024-11-29', '2024-12-01'),
(8, 2, 'The Stranger', 'Albert Camus', 'Vintage International', 1989, 843, '2024-12-01', '2024-12-05'),
(9, 11, 'The Brothers Karamazov', 'Fyodor Dostoevsky', 'Farrar, Straus and Giroux', 2002, 891, '2024-12-20', '2024-12-24'),
(10, 9, 'Great Expectations', 'Charles Dickens', 'Oxfor University Press', 1998, 823, '2024-12-03', '2024-12-05');

-- --------------------------------------------------------

--
-- Table structure for table `borrower`
--

CREATE TABLE `borrower` (
  `borrowID` int(11) NOT NULL,
  `borrowerName` varchar(255) NOT NULL,
  `borrowDate` date DEFAULT NULL,
  `returnDate` date DEFAULT NULL,
  `book_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `borrower`
--

INSERT INTO `borrower` (`borrowID`, `borrowerName`, `borrowDate`, `returnDate`, `book_ID`) VALUES
(1, 'Jiro Carag', '2024-12-02', '2024-12-04', 4),
(2, 'Mira Balino', '2024-12-01', '2024-12-05', 8),
(3, 'JIRO CARAG', '2024-12-07', '2024-12-10', 1),
(4, 'Alexis Erlano', '2024-12-07', '2024-12-09', 1),
(5, 'Aloy Espejo', '2024-12-09', '2024-12-11', 3),
(6, 'Shaine Gonzales', '2024-12-02', '2024-12-05', 5),
(7, 'Joshua Maranan', '2024-12-12', '2024-12-15', 2),
(8, 'Mcky Ongcal', '2024-11-29', '2024-12-01', 7),
(9, 'Joshua Maranan', '2024-12-03', '2024-12-05', 10),
(10, 'Deniel Quizzagan', '2024-12-07', '2024-12-08', 6),
(11, 'KB Atienza', '2024-12-20', '2024-12-24', 9);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`book_ID`);

--
-- Indexes for table `borrowedbooks`
--
ALTER TABLE `borrowedbooks`
  ADD PRIMARY KEY (`book_ID`,`borrowID`),
  ADD KEY `borrowID` (`borrowID`);

--
-- Indexes for table `borrower`
--
ALTER TABLE `borrower`
  ADD PRIMARY KEY (`borrowID`),
  ADD KEY `book_ID` (`book_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `book_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `borrower`
--
ALTER TABLE `borrower`
  MODIFY `borrowID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `borrowedbooks`
--
ALTER TABLE `borrowedbooks`
  ADD CONSTRAINT `borrowedbooks_ibfk_1` FOREIGN KEY (`book_ID`) REFERENCES `books` (`book_ID`),
  ADD CONSTRAINT `borrowedbooks_ibfk_2` FOREIGN KEY (`borrowID`) REFERENCES `borrower` (`borrowID`);

--
-- Constraints for table `borrower`
--
ALTER TABLE `borrower`
  ADD CONSTRAINT `borrower_ibfk_1` FOREIGN KEY (`book_ID`) REFERENCES `books` (`book_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
