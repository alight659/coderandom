CREATE DATABASE library;
USE library;
CREATE table books (
id INT PRIMARY KEY AUTO_INCREMENT,
title VARCHAR(255) NOT NULL,
author VARCHAR(255) NOT NULL,
year INT NOT NULL
);