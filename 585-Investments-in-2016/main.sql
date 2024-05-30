-- note: Since we can't use columns that are not in the GROUP BY clause, we used MIN() on them. Now since there's only one record
-- for each unique lat, lon, using MIN(x) will get us the actual x ITSELF.
WITH unique_tiv2016 AS (SELECT MIN(pid)      AS pid,
                               MIN(tiv_2016) AS tiv_2016,
                               MIN(tiv_2015) AS tiv_2015
                        FROM Insurance
                        GROUP BY lat, lon
                        HAVING COUNT(pid) = 1 -- should be unique
)

SELECT ROUND(SUM(t1.tiv_2016)::decimal, 2) AS tiv_2016 -- ::decimal is important here
FROM unique_tiv2016 AS t1
WHERE EXISTS (SELECT 1 -- have the same tiv_2015 value as one or more other policyholders?
              FROM Insurance AS i
              WHERE i.pid != t1.pid -- should be another row not the same row, we do this using the primary key
                AND i.tiv_2015 = t1.tiv_2015);