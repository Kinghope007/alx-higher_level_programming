-- Thi SQL script cretes the second_table and inserts record
-- create the second_table if it doesn't exist
-- Insert records into the second_table

CREATE TABLE IF NOT EXISTS hbtn_0c_0.second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO hbtn_0c_0.second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
