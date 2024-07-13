-- Approach 1: Return the First n Rows Using Correlated Subquery
-- https://leetcode.com/problems/department-top-three-salaries/solutions/3203554/sql-department-top-three-salaries/?envType=study-plan-v2&envId=top-sql-50
Select d.name as department, e1.name as employee, e1.salary as Salary
From Employee e1
         join Department d on e1.DepartmentId = d.Id
Where 3 > (select count(distinct (e2.Salary))
           from Employee e2
           where e2.Salary > e1.Salary
             and e1.DepartmentId = e2.DepartmentId);

----------------------
-- Approach 2: Return the First n Rows Using DENSE_RANK()
with employee_department as (select d.id,
                                    d.name                                                       as "Department",
                                    e.salary                                                     as "Salary",
                                    e.name                                                       as "Employee",
                                    dense_rank() over (partition by d.id order by e.salary desc) as rnk
                             from department d
                                      join employee e
                                           on d.id = e.departmentId)
select "Department", "Employee", "Salary"
from employee_department
where rnk <= 3;
