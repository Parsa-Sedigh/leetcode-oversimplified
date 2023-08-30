select e1.name
from Employee e1
         inner join Employee e2 on e1.id = e2.managerId
group by e1.managerId, e1.id
having count(e1.id) >= 5;

-- approach 2
select name
from employee
where id in
      (select managerId
       from Employee
       group by managerId
       having count(managerId) >= 5);