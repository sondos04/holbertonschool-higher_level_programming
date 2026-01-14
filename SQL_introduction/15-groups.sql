-- list the numbers of score recods

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score;
