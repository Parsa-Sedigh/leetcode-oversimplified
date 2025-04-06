with emp_id_with_number_of_depts as (select employee_id, count(department_id) dept_count
                                     from employee
                                     group by employee_id)

select e.employee_id, e.department_id
from employee e
         inner join emp_id_with_number_of_depts as ed on (e.employee_id = ed.employee_id)
where primary_flag = 'Y'
   or ed.dept_count = 1
