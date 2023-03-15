--  lists the number of records with the same score in the table second_table
-- Query to list number of records with same score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
