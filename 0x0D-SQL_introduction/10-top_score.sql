-- Write a script that lists all records of the table second of the database hbtn_0c_0 in your MySQL
-- Result should display both the score and the name
-- Records should be ordered by score
-- The database name will be passed as an argument of the mysql command
SELECT score, name FROM second_table ORDER BY score DESC;