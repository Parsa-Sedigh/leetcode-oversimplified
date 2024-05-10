-- note: We can't put the sub-query in SELECT. We have to put it in FROM. Because we need the result of window func and
-- we know window func are evaluated lately. So we put the sub-query that has the window func calculation in FROM and since
-- FROM is evaluated first, we have access to window func result in the WHERE clause.

select person_name
from (select *, sum(weight) over (order by turn) as total_weight
      from queue)
where total_weight <= 1000
order by total_weight desc
limit 1