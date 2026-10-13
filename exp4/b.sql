-- Table WITHOUT constraints
CREATE TABLE Student_Basic (
student_id INT,
name VARCHAR(50),
dept VARCHAR(20),
cgpa FLOAT
);
-- Table WITH constraints
CREATE TABLE Student (
student_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50) NOT NULL,
email VARCHAR(80) UNIQUE,
dept_id INT NOT NULL,
cgpa DECIMAL(4,2) DEFAULT 0.0 CHECK (cgpa >= 0 AND cgpa <= 10),
join_date DATE DEFAULT (CURRENT_DATE)
);
-- View all tables
SHOW TABLES;
-- View table structure
DESC Student;
DESCRIBE Student;
