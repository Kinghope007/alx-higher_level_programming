-- This SQL script list the record with score >= 10
-- Select records with score >= 10 in descending order

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
