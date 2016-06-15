-- Adminer 4.1.0 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `client`;
CREATE TABLE `client` (
  `idClient` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `lastName` varchar(200) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `amount` float NOT NULL,
  `consecutive` int(11) NOT NULL DEFAULT '1',
  `maxCode` int(11) NOT NULL DEFAULT '100',
  `state` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0:registrada  1:aprobada  2:negada',
  PRIMARY KEY (`idClient`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `idEmployee` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `lastName` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`idEmployee`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `transactions`;
CREATE TABLE `transactions` (
  `idTransaction` bigint(20) NOT NULL AUTO_INCREMENT,
  `codeTransaction` varchar(100) NOT NULL COMMENT '[idClient]-[consecutivo]',
  `typeTransaction` smallint(6) NOT NULL COMMENT '0:Consignacion   1: Retiro  2: Transferencia',
  `amount` float NOT NULL,
  `idClientFrom` bigint(20) NOT NULL,
  `idClientTo` bigint(20) DEFAULT NULL,
  `state` smallint(6) NOT NULL COMMENT '0:registrada 1:aprobada  2:negada',
  PRIMARY KEY (`idTransaction`),
  KEY `idClientFrom` (`idClientFrom`),
  KEY `idClientTo` (`idClientTo`),
  CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`idClientFrom`) REFERENCES `client` (`idClient`),
  CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`idClientTo`) REFERENCES `client` (`idClient`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- 2016-06-15 22:38:11
