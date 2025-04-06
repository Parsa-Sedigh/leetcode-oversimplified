-- window function
select distinct visited_on,
                sum(amount) over (order by visited_on range between '6 day' preceding and current row) as amount,
                round(sum(amount) over (order by visited_on range between '6 day' preceding and current row) / 7.,
                      2)                                                                               as average_amount
from customer
order by visited_on
offset 6;

--
WITH last_6_days AS (SELECT DISTINCT visited_on
                     FROM Customer
                     ORDER BY visited_on ASC
                     OFFSET 6)

SELECT c1.visited_on,
       SUM(c2.amount)                AS amount,
       ROUND(SUM(c2.amount) / 7., 2) AS average_amount
FROM last_6_days AS c1
         INNER JOIN Customer AS c2
                    ON c2.visited_on BETWEEN c1.visited_on - 6 AND c1.visited_on
GROUP BY c1.visited_on;