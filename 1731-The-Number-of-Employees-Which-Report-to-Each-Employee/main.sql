-- Note: Do not make the mistake: manager's reports_to should be null. Because managers could report to someone else themselves.
-- Note: The reporters are the employees that their reports_to is not null, but among these reporters, we could have managers.
-- The employees that have reports_to set to null are definitely managers.
-- But let's say empl_1 reports_to is not null, he's considered a reporter and if some other employee has it's reports_to
-- set to the id of this empl_1, then empl_1 is considered a manager as well.

-- you could name this CTE: managers as well. Because the data returned here is the data of some employees that are reporting to
-- someone but these could be managers themselves as well.
with reporters as (select reports_to, count(reports_to) as reports_count, round(avg(age)) as average_age
                   from employees
                   where reports_to is not null
                   group by reports_to)

select e.employee_id, e.name, r.reports_count, r.average_age
from reporters r
         inner join employees e on r.reports_to = e.employee_id
order by e.employee_id