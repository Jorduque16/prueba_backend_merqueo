CREATE DATABASE  IF NOT EXISTS `pruebamerqueo` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `pruebamerqueo`;
-- MySQL dump 10.13  Distrib 8.0.19, for Linux (x86_64)
--
-- Host: jorduque.c1dq0udmtqkk.us-east-1.rds.amazonaws.com    Database: pruebamerqueo
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` varchar(45) NOT NULL,
  `quantity` tinyint(10) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id_index` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,'1',3,'2019-03-01'),(2,'2',3,'2019-03-01'),(3,'3',7,'2019-03-01'),(4,'4',8,'2019-03-01'),(5,'5',10,'2019-03-01'),(6,'6',15,'2019-03-01'),(7,'7',26,'2019-03-01'),(8,'8',11,'2019-03-01'),(9,'9',1,'2019-03-01'),(10,'10',8,'2019-03-01'),(11,'11',7,'2019-03-01'),(12,'12',8,'2019-03-01'),(13,'13',2,'2019-03-01'),(14,'14',1,'2019-03-01'),(15,'15',1,'2019-03-01'),(16,'16',9,'2019-03-01'),(17,'17',17,'2019-03-01'),(18,'18',8,'2019-03-01'),(19,'19',9,'2019-03-01'),(20,'20',9,'2019-03-01'),(21,'21',3,'2019-03-01'),(22,'22',6,'2019-03-01'),(23,'23',9,'2019-03-01'),(24,'24',9,'2019-03-01'),(25,'25',10,'2019-03-01'),(26,'26',40,'2019-03-01'),(27,'27',2,'2019-03-01'),(28,'28',3,'2019-03-01'),(29,'29',2,'2019-03-01'),(30,'30',1,'2019-03-01'),(31,'31',9,'2019-03-01'),(32,'32',10,'2019-03-01'),(33,'33',2,'2019-03-01'),(34,'34',3,'2019-03-01'),(35,'35',3,'2019-03-01'),(36,'36',6,'2019-03-01');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_products`
--

DROP TABLE IF EXISTS `order_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` varchar(45) NOT NULL,
  `order_id` varchar(45) NOT NULL,
  `quantity` tinyint(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id_index` (`product_id`),
  KEY `order_id_index` (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_products`
--

LOCK TABLES `order_products` WRITE;
/*!40000 ALTER TABLE `order_products` DISABLE KEYS */;
INSERT INTO `order_products` VALUES (1,'1','1',1),(2,'2','1',21),(3,'37','1',7),(4,'3','1',10),(5,'4','1',5),(6,'5','2',100),(7,'6','2',60),(8,'7','3',4),(9,'8','3',3),(10,'9','3',4),(11,'10','3',8),(12,'11','3',5),(13,'12','4',3),(14,'13','4',2),(15,'14','4',4),(16,'4','4',2),(17,'15','4',3),(18,'16','5',127),(19,'17','6',2),(20,'18','6',3),(21,'15','6',2),(22,'19','6',2),(23,'20','6',3),(24,'21','7',3),(25,'22','7',2),(26,'23','7',2),(27,'39','7',4),(28,'24','7',15),(29,'25','8',3),(30,'26','8',2),(31,'22','8',4),(32,'27','8',1),(33,'5','8',1),(34,'22','9',1),(35,'28','15',1),(36,'7','10',1),(37,'41','11',1),(38,'19','11',6),(39,'29','11',1),(40,'17','11',1),(41,'30','11',1),(42,'7','12',1),(43,'25','12',2),(44,'5','12',1),(45,'31','12',25),(46,'43','13',1),(47,'30','13',1),(48,'32','13',1),(49,'33','13',1),(50,'28','13',2),(51,'16','14',3),(52,'34','14',3),(53,'35','14',3),(54,'12','14',1),(55,'36','14',1);
/*!40000 ALTER TABLE `order_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(45) NOT NULL,
  `priority` tinyint(1) NOT NULL,
  `address` varchar(45) NOT NULL,
  `delivery_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id_index` (`user_id`),
  KEY `delivery_date_index` (`delivery_date`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'1',1,'KR 14 # 87 - 20','2019-03-01'),(2,'2',1,'KR 20 # 164A - 5','2019-03-01'),(3,'3',3,'KR 13 # 74 - 38','2019-03-01'),(4,'4',1,'CL 93 # 12 - 9','2019-03-01'),(5,'5',1,'CL 71 # 3 - 74','2019-03-01'),(6,'6',2,'KR 20 # 134A - 5','2019-03-01'),(7,'7',2,'CL 80 # 14 - 38','2019-03-01'),(8,'8',7,'KR 14 # 98 - 74','2019-03-01'),(9,'9',1,'KR 58 # 93 - 1','2019-03-01'),(10,'10',1,'CL 93B # 17 - 12','2019-03-01'),(11,'11',10,'KR 68D # 98A - 11','2019-03-01'),(12,'12',2,'AC 72 # 20 - 4','2019-03-01'),(13,'13',3,'KR 22 # 122 - 57','2019-03-01'),(14,'14',8,'KR 88 # 72A - 26','2019-03-01'),(15,'1',9,'KR 14 # 87 - 20','2019-03-01');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Leche'),(2,'Huevos'),(3,'Manzana Verde'),(4,'Pepino Cohombro'),(5,'Pimentón Rojo'),(6,'Kiwi'),(7,'Cebolla Cabezona Blanca Limpia'),(8,'Habichuela'),(9,'Mango Tommy Maduro'),(10,'Tomate Chonto Pintón'),(11,'Zanahoria Grande'),(12,'Aguacate Maduro'),(13,'Kale o Col Rizada'),(14,'Cebolla Cabezona Roja Limpia'),(15,'Tomate Chonto Maduro'),(16,'Acelga'),(17,'Espinaca Bogotana x 500grs'),(18,'Ahuyama'),(19,'Cebolla Cabezona Blanca Sin Pelar'),(20,'Melón'),(21,'Cebolla Cabezona Roja Sin Pelar'),(22,'Cebolla Larga Junca x 500grs'),(23,'Hierbabuena x 500grs'),(24,'Lechuga Crespa Verde'),(25,'Limón Tahití'),(26,'Mora de Castilla'),(27,'Pimentón Verde'),(28,'Tomate Larga Vida Maduro'),(29,'Cilantro x 500grs'),(30,'Fresa Jugo'),(31,'Papa R-12 Mediana'),(32,'Curuba'),(33,'Brocolí'),(34,'Aguacate Hass Pintón'),(35,'Aguacate Hass Maduro'),(36,'Aguacate Pintón'),(37,'Pan Bimbo'),(38,NULL),(39,'Lechuga Crespa Morada'),(40,''),(41,'Banano'),(42,NULL),(43,'Banano'),(44,NULL),(45,NULL),(46,NULL),(47,NULL);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provider_products`
--

DROP TABLE IF EXISTS `provider_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provider_products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provider_id` varchar(45) NOT NULL,
  `product_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `provider_id_index` (`provider_id`),
  KEY `product_id_index` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provider_products`
--

LOCK TABLES `provider_products` WRITE;
/*!40000 ALTER TABLE `provider_products` DISABLE KEYS */;
INSERT INTO `provider_products` VALUES (1,'1','1'),(2,'1','2'),(3,'1','45'),(4,'1','3'),(5,'1','4'),(6,'1','5'),(7,'1','46'),(8,'1','24'),(9,'1','25'),(10,'1','26'),(11,'1','27'),(12,'2','28'),(13,'2','47'),(14,'2','29'),(15,'2','30'),(16,'2','31'),(17,'2','32'),(18,'2','33'),(19,'2','34'),(20,'2','35'),(21,'2','36'),(22,'2','16'),(23,'2','17'),(24,'3','6'),(25,'3','7'),(26,'3','8'),(27,'3','9'),(28,'3','10'),(29,'3','11'),(30,'3','12'),(31,'3','13'),(32,'3','14'),(33,'3','15'),(34,'3','18'),(35,'3','19'),(36,'3','20'),(37,'3','21'),(38,'3','22'),(39,'3','23');
/*!40000 ALTER TABLE `provider_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `providers`
--

DROP TABLE IF EXISTS `providers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `providers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `providers`
--

LOCK TABLES `providers` WRITE;
/*!40000 ALTER TABLE `providers` DISABLE KEYS */;
INSERT INTO `providers` VALUES (1,'Ruby'),(2,'Raul'),(3,'Angelica');
/*!40000 ALTER TABLE `providers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Sofia'),(2,'Angel'),(3,'Hocks'),(4,'Michael'),(5,'Bar de Alex'),(6,'Sabor Criollo'),(7,'El Pollo Rojo'),(8,'All Salad'),(9,'Parrilla y sabor'),(10,'restaurante yerbabuena'),(11,'Luis David'),(12,'David Carruyo'),(13,'MARIO'),(14,'Harold');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-31  1:16:54