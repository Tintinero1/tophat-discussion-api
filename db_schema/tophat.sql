CREATE DATABASE  IF NOT EXISTS `tophat_discussion_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `tophat_discussion_db`;
-- MySQL dump 10.13  Distrib 8.0.30, for Linux (x86_64)
--
-- Host: %    Database: tophat_discussion_db
-- ------------------------------------------------------
-- Server version	8.0.30

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

--
-- Table structure for table `Comment`
--

DROP TABLE IF EXISTS `Comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Comment` (
  `ID_Comment` int NOT NULL AUTO_INCREMENT,
  `Started_by` varchar(45) NOT NULL,
  `Comment` varchar(500) NOT NULL,
  PRIMARY KEY (`ID_Comment`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comment`
--

LOCK TABLES `Comment` WRITE;
/*!40000 ALTER TABLE `Comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `Comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Discussion_Question`
--

DROP TABLE IF EXISTS `Discussion_Question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Discussion_Question` (
  `ID_Discussion_Question` int NOT NULL AUTO_INCREMENT,
  `Started_by` varchar(45) NOT NULL,
  `Question` varchar(500) NOT NULL,
  PRIMARY KEY (`ID_Discussion_Question`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Discussion_Question`
--

LOCK TABLES `Discussion_Question` WRITE;
/*!40000 ALTER TABLE `Discussion_Question` DISABLE KEYS */;
/*!40000 ALTER TABLE `Discussion_Question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rel_Comment_Response`
--

DROP TABLE IF EXISTS `Rel_Comment_Response`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Rel_Comment_Response` (
  `ID_Rel_Comment_Response` int NOT NULL AUTO_INCREMENT,
  `FK_ID_Comment` int NOT NULL COMMENT 'ID of the comment (Table Comment) to be related with the response',
  `FK_ID_Response` int NOT NULL COMMENT 'ID of the response (Table Comment) to be related with the comment',
  PRIMARY KEY (`ID_Rel_Comment_Response`),
  KEY `fk_Rel_Comment_Response_ID_Comment_idx` (`FK_ID_Comment`),
  KEY `fk_Rel_Comment_Response_ID_Response_idx` (`FK_ID_Response`),
  CONSTRAINT `fk_Rel_Comment_Response_ID_Comment` FOREIGN KEY (`FK_ID_Comment`) REFERENCES `Comment` (`ID_Comment`),
  CONSTRAINT `fk_Rel_Comment_Response_ID_Response` FOREIGN KEY (`FK_ID_Response`) REFERENCES `Comment` (`ID_Comment`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rel_Comment_Response`
--

LOCK TABLES `Rel_Comment_Response` WRITE;
/*!40000 ALTER TABLE `Rel_Comment_Response` DISABLE KEYS */;
/*!40000 ALTER TABLE `Rel_Comment_Response` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rel_Discussion_Question_Response`
--

DROP TABLE IF EXISTS `Rel_Discussion_Question_Response`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Rel_Discussion_Question_Response` (
  `ID_Rel_Discussion_Question_Response` int NOT NULL AUTO_INCREMENT,
  `FK_ID_Discussion_Question` int NOT NULL,
  `FK_ID_Comment` int NOT NULL,
  PRIMARY KEY (`ID_Rel_Discussion_Question_Response`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rel_Discussion_Question_Response`
--

LOCK TABLES `Rel_Discussion_Question_Response` WRITE;
/*!40000 ALTER TABLE `Rel_Discussion_Question_Response` DISABLE KEYS */;
/*!40000 ALTER TABLE `Rel_Discussion_Question_Response` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'tophat_discussion_db'
--

--
-- Dumping routines for database 'tophat_discussion_db'
--
/*!50003 DROP PROCEDURE IF EXISTS `sp_Create_Comment` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`tophat`@`%` PROCEDURE `sp_Create_Comment`(
    IN prm_started_by varchar(45),
    IN prm_comment varchar(500),
    OUT prm_id_comment INT
)
BEGIN

INSERT INTO `tophat_discussion_db`.Comment (Started_by, Comment)
VALUES (prm_started_by, prm_comment);

SET prm_id_comment = (SELECT LAST_INSERT_ID());
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_Create_Discussion_Question` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`tophat`@`%` PROCEDURE `sp_Create_Discussion_Question`(
	IN prm_started_by varchar(45),
    IN prm_question varchar(500),
    OUT prm_id_discussion_question INT
)
BEGIN

/*Validates that discussion question does not exists*/
DECLARE prm_id_dis_ques INT DEFAULT 0;
SET prm_id_dis_ques = IFNULL((SELECT ID_Discussion_Question FROM `tophat_discussion_db`.Discussion_Question WHERE Question = prm_question),0);

IF prm_id_dis_ques = 0 THEN
	INSERT INTO `tophat_discussion_db`.Discussion_Question (Started_by, Question)
	VALUES (prm_started_by, prm_question);
END IF;

SET prm_id_discussion_question = (SELECT LAST_INSERT_ID());
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_Create_Rel_Comment_Response` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`tophat`@`%` PROCEDURE `sp_Create_Rel_Comment_Response`(
	IN prm_fk_id_comment INT,
    IN prm_fk_id_response INT
)
BEGIN

/*Validates that comment and response already exists*/
DECLARE prm_comment_exists INT DEFAULT 0;
DECLARE prm_response_exists INT DEFAULT 0;

SET prm_comment_exists = IFNULL((SELECT ID_Comment from `tophat_discussion_db`.Comment WHERE ID_Comment = prm_fk_id_comment),0);
SET prm_response_exists = IFNULL((SELECT ID_Comment from `tophat_discussion_db`.Comment WHERE ID_Comment = prm_fk_id_response),0);

IF prm_comment_exists != 0 and prm_response_exists != 0 THEN
	INSERT INTO `tophat_discussion_db`.Rel_Comment_Response (FK_ID_Comment, FK_ID_Response)
	VALUES (prm_fk_id_comment, prm_fk_id_response);
END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_Create_Rel_Discussion_Question_Response` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`tophat`@`%` PROCEDURE `sp_Create_Rel_Discussion_Question_Response`(
	IN prm_question varchar(500),
    IN prm_fk_id_response INT
)
BEGIN
DECLARE prm_discussion_exists INT DEFAULT 0;
DECLARE prm_response_exists INT DEFAULT 0;

/*Validates that discussion question already exists*/
SET prm_discussion_exists = IFNULL((SELECT ID_Discussion_Question 
									from `tophat_discussion_db`.Discussion_Question 
                                    WHERE Question = prm_question),0);

/*Validates response already exists*/
SET prm_response_exists = IFNULL((SELECT ID_Comment 
									from `tophat_discussion_db`.Comment 
									WHERE ID_Comment = prm_fk_id_response),0);
SELECT(prm_response_exists);
IF prm_discussion_exists != 0 and prm_response_exists != 0 THEN
	INSERT INTO `tophat_discussion_db`.Rel_Discussion_Question_Response (FK_ID_Discussion_Question, FK_ID_Comment)
	VALUES (prm_discussion_exists, prm_response_exists);
END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_ERASE_ALL_DATA` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`tophat`@`%` PROCEDURE `sp_ERASE_ALL_DATA`()
BEGIN
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE table Comment;
TRUNCATE table Discussion_Question;
TRUNCATE table Rel_Comment_Response;
TRUNCATE table Rel_Discussion_Question_Response;

SET FOREIGN_KEY_CHECKS = 1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_Read_Comments` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`tophat`@`%` PROCEDURE `sp_Read_Comments`(
	IN prm_question varchar(500)
)
BEGIN

Select c.ID_Comment, c.Started_by, c.Comment 
from Comment as c
INNER JOIN Discussion_Question as DQ
on DQ.ID_Discussion_Question = c.FK_ID_Discussion_Question
WHERE DQ.Question = prm_question;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_Read_Discussion` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`tophat`@`%` PROCEDURE `sp_Read_Discussion`(
	IN prm_question varchar(500)
)
BEGIN

SELECT ID_Discussion_Question, Started_by, Question
FROM `tophat_discussion_db`.Discussion_Question 
WHERE Question = prm_question;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_Read_Discussion_Question` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`tophat`@`%` PROCEDURE `sp_Read_Discussion_Question`(
	IN prm_question varchar(500),
    OUT prm_ID_Discussion_Question INT
)
BEGIN

SET prm_ID_Discussion_Question = IFNULL((	SELECT ID_Discussion_Question 
											FROM `tophat_discussion_db`.Discussion_Question WHERE Question = prm_question),0);

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_Read_Discussion_Response` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`tophat`@`%` PROCEDURE `sp_Read_Discussion_Response`(
	IN prm_question varchar(500)
)
BEGIN

SELECT C.ID_Comment, C.Started_by, C.Comment 
FROM Discussion_Question AS DQ
INNER JOIN Rel_Discussion_Question_Response AS RDQR
ON RDQR.FK_ID_Discussion_Question = DQ.ID_Discussion_Question
INNER JOIN Comment AS C
ON C.ID_Comment = RDQR.FK_ID_Comment
WHERE DQ.Question = prm_question;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_Read_Responses` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`tophat`@`%` PROCEDURE `sp_Read_Responses`(
	IN prm_id_comment INT
)
BEGIN

Select c2.ID_Comment, c2.Started_by, c2.Comment 
from Rel_Comment_Response
INNER JOIN Comment as c
on c.ID_Comment = Rel_Comment_Response.FK_ID_Comment
INNER JOIN Comment as c2
on c2.ID_Comment = Rel_Comment_Response.FK_ID_Response
WHERE c.ID_Comment = prm_id_comment;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-23 14:24:45
