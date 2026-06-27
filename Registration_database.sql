CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(15),
    gender VARCHAR(10),
    dob DATE,
    course VARCHAR(50),
    address VARCHAR(200)
);

Select * from Students;