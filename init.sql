-- Create database if not exists
CREATE DATABASE IF NOT EXISTS edu_database;
USE edu_database;

-- Create table
CREATE TABLE IF NOT EXISTS students (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    city_of_birth VARCHAR(255) NULL,
    grade INT NOT NULL
);

-- Load data from CSV into the table
LOAD DATA LOCAL INFILE '/home/vadym_nakytniak/data/students_info.csv'
INTO TABLE students
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, email, first_name, last_name, city_of_birth, grade);
