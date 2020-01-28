DROP DATABASE aap;
CREATE DATABASE aap;
USE aap;
#SET SQL_SAFE_UPDATES = 0;
ALTER DATABASE aap CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

CREATE TABLE `Users` (
  `user_id` int UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(100) NOT NULL,
  `username` VARCHAR(100) UNIQUE NOT NULL,
  `ASECert_id` VARCHAR(100),
  `address` VARCHAR(100) NOT NULL,
  `bio` VARCHAR(5000),
  `paypal_info` VARCHAR(100),
  `ASECert_HTTP` VARCHAR(100)
);

CREATE TABLE `Permissions` (
  `permission_id` int UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `permission_name` VARCHAR(100)
);

CREATE TABLE `User_Permissions` (
  `permission_id` int,
  `user_id` int
);

CREATE TABLE `Qualification` (
  `qual_id` int UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `qualification_name` VARCHAR(100)
);

CREATE TABLE `Mechanics_Qualifications` (
  `qual_id` int,
  `mec_id` int
);

CREATE TABLE `Job_Types` (
  `job_type_id` int UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `job_name` VARCHAR(100),
  `HHTP_Link` VARCHAR(200)
);

CREATE TABLE `Job_Qualifications` (
  `qual_id` int,
  `job_type_id` int
);

CREATE TABLE `Master_Parts_list` (
  `parts_id` int UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `part_name` VARCHAR(100)
);

CREATE TABLE `Parts_List_for_Job` (
  `parts_id` int,
  `job_type_id` int
);

CREATE TABLE `Jobs` (
  `job_id` int UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `job_type_id` int,
  `location` point,
  `address` VARCHAR(100),
  `details` VARCHAR(4000),
  `cus_id` int
);

CREATE TABLE `Bookings` (
  `job_id` int,
  `store_id` int,
  `mec_id` int
);

CREATE TABLE `Status` (
  `status_id` int UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `status_name` VARCHAR(100)
);

CREATE TABLE `Status_list` (
  `status_id` int,
  `job_id` int,
  `status_update` VARCHAR(100),
  `status_time` timestamp
);

CREATE TABLE `Store` (
  `store_id` int UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `store_address` VARCHAR(100),
  `location` point
);

ALTER TABLE `Mechanics_Qualifications` ADD FOREIGN KEY (`qual_id`) REFERENCES `Qualification` (`qual_id`);

ALTER TABLE `Jobs` ADD FOREIGN KEY (`job_type_id`) REFERENCES `Job_Types` (`job_type_id`);

ALTER TABLE `Bookings` ADD FOREIGN KEY (`job_id`) REFERENCES `Jobs` (`job_id`);

ALTER TABLE `Bookings` ADD FOREIGN KEY (`store_id`) REFERENCES `Store` (`store_id`);

ALTER TABLE `Parts_List_for_Job` ADD FOREIGN KEY (`job_type_id`) REFERENCES `Job_Types` (`job_type_id`);

ALTER TABLE `Mechanics_Qualifications` ADD FOREIGN KEY (`mec_id`) REFERENCES `Users` (`user_id`);

ALTER TABLE `Bookings` ADD FOREIGN KEY (`mec_id`) REFERENCES `Users` (`user_id`);

ALTER TABLE `User_Permissions` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`);

ALTER TABLE `Jobs` ADD FOREIGN KEY (`cus_id`) REFERENCES `Users` (`user_id`);

ALTER TABLE `Parts_List_for_Job` ADD FOREIGN KEY (`parts_id`) REFERENCES `Master_Parts_list` (`parts_id`);

ALTER TABLE `Job_Qualifications` ADD FOREIGN KEY (`qual_id`) REFERENCES `Qualification` (`qual_id`);

ALTER TABLE `Job_Qualifications` ADD FOREIGN KEY (`job_type_id`) REFERENCES `Job_Types` (`job_type_id`);

ALTER TABLE `Status_list` ADD FOREIGN KEY (`status_id`) REFERENCES `Status` (`status_id`);

ALTER TABLE `Status_list` ADD FOREIGN KEY (`job_id`) REFERENCES `Jobs` (`job_id`);

ALTER TABLE `User_Permissions` ADD FOREIGN KEY (`permission_id`) REFERENCES `Permissions` (`permission_id`);
