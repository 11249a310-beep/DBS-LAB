-- Disable auto-commit first
SET autocommit = 0;
-- OR
START TRANSACTION;
-- Insert a student
INSERT INTO Student (name, email, dept_id, cgpa) VALUES ('Test', 'test@m.com', 1,
5.0);
SELECT * FROM Student; -- Shows the new row
-- SAVE the transaction permanently
COMMIT;
-- Another transaction:
START TRANSACTION;
UPDATE Student SET cgpa = 0.0 WHERE dept_id = 1; -- Accidental update!
SELECT * FROM Student; -- Shows changed data
-- UNDO the transaction (nothing was saved)
ROLLBACK;
SELECT * FROM Student; -- Original data restored!
-- SAVEPOINT (partial rollback)
START TRANSACTION;
INSERT INTO Student (name,email,dept_id,cgpa) VALUES ('A','a@m.com',1,9.0);
SAVEPOINT sp1;
INSERT INTO Student (name,email,dept_id,cgpa) VALUES ('B','b@m.com',2,8.0);
ROLLBACK TO sp1; -- Undoes only the second insert
COMMIT; -- Commits first insert only
