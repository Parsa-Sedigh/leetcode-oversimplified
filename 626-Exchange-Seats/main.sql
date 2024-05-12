select id,
       case
           -- edge case: the last row should use it's own `student` col not the after(lead()) or the one at the before(lag())
           when id % 2 = 1 and lead(student) over (order by id) is null then student
           when id % 2 = 0 then lag(student) over (order by id)
           else lead(student) over (order by id)
           end as student
from seat