-- This SQL script lists the number of records.
-- Count records for each score and display the result
SELECT 
    score,
    COUNT(*) AS number
FROM 
    hbtn_0c_0.second_table
GROUP BY 
    score
ORDER BY 
    number DESC;
