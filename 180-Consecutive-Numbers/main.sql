-- Note: we can't use ORDER BY for the whole select, instead, we need to use ORDER BY inside over() . Because SELECT(aggregate funcs inside
-- SELECT) are executed before overall ORDER BY of the query.

-- Note: We also need to check for ids being consecutive.

with cte as (select num                             as num1,
                    lead(num, 1) over (order by id) as num2,
                    lead(num, 2) over (order by id) as num3,
                    id                              as id1,
                    lead(id, 1) over (order by id)  as id2,
                    lead(id, 2) over (order by id)  as id3
             from logs)

select distinct num1 as "ConsecutiveNums"
from cte
where num1 = num2
  and num2 = num3
  and id2 = id1 + 1
  and id3 = id2 + 1