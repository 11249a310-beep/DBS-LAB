-- INSERT single row
INSERT INTO Student (name, email, dept_id, cgpa)
VALUES ('Priya S', 'priya@mail.com', 1, 9.2);

-- INSERT multiple rows
INSERT INTO Student (name, email, dept_id, cgpa) VALUES
('Arjun K', 'arjun@mail.com', 2, 8.7),
('Deepika R', 'deepika@mail.com',1, 9.5),
('Ravi M', 'ravi@mail.com', 3, 7.8),
('Kavya P', 'kavya@mail.com', 1, 8.9);
-- VIEW all records
SELECT * FROM Student;
-- UPDATE a record
UPDATE Student SET cgpa = 9.0 WHERE name = 'Ravi M';
-- DELETE a record
DELETE FROM Student WHERE student_id = 5;
-- DELETE with condition
DELETE FROM Student WHERE cgpa < 8.0;
