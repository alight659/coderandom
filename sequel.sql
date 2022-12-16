--PRG1
CREATE TABLE student(
    rollno INT NOT NULL PRIMARY KEY,
    sname VARCHAR(100) NOT NULL,
    maths varchar(3),
    stream varchar(4));

INSERT INTO student VALUES (1, "S1",22,"pcm"),(2, "S2",34,"pcm"),(3, "S3",40,"pcbm"),(4,"S4",32,"pcbm");
--a
ALTER TABLE student ADD cs char(3);
ALTER TABLE student MODIFY COLUMN cs varchar(3);
ALTER TABLE student DROP column cs;
--b
UPDATE student SET maths = 23 where rollno = 1;
--c
SELECT * FROM student ORDER BY maths DESC;
SELECT * FROM student ORDER BY maths ASC;
--d
DELETE FROM student WHERE rollno = 4;
--e
SELECT MIN(maths), MAX(maths), SUM(maths), AVG(maths) FROM student;
SELECT stream, COUNT(stream) FROM student GROUP BY stream;

--PRG2
--a
SELECT * FROM MOVIE;
--b
SELECT MovieID, MovieName, BusinessCost+ProductionCost as "Total_Earning" FROM MOVIE;
--c
SELECT DISTINCT Category FROM MOVIE;
--d
SELECT MovieID, MovieName, BusinessCost-ProductionCost as "NetProfit" FROM MOVIE;
--e
SELECT MovieID, MovieName, ProductionCost+BusinessCost as "Cost" FROM MOVIE WHERE ProductionCost < 100000 AND ProductionCost > 10000;
--f
SELECT * FROM MOVIE WHERE Category IN ("Comedy","Action");
--g
SELECT * FROM MOVIE WHERE ReleaseDate > CURRENT_DATE;