-- this doesn't work
    -------------
-- select * from myNumbers
-- group by num
-- having count(*) = 1
-- order by num desc
-- limit 1

-- https://bernardoamc.github.io/sql/2015/05/04/group-by-non-aggregate-columns/

select max(num) as num
from (select num
      from myNumbers
      group by num
      having count(*) = 1)
limit 1