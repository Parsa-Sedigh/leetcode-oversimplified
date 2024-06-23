-- approach 1:
select -- we need another select to get a NULL in absence of a value.
    -- note: distinct is important here, because we could have:
    -- 100
    -- 100
    -- as the values. Here, there is no second highest salary, so we need to only consider the unique values.
    (select distinct salary as SecondHighestSalary from Employee
     order by salary desc
     offset 1 limit 1);

----------

-- approach 2:
-- aggregate functions always return a row, defaulting to NULL in absence of a value.

with highest_salary as (select max(salary) as salary
                        from employee)
select max(salary) as "SecondHighestSalary"
from employee
-- this effectively gives us the SECOND highest salary.
where salary < (select salary
                from highest_salary);