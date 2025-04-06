-- JOIN

SELECT e1.employee_id
FROM Employees e1
         LEFT JOIN Employees e2
                   ON e1.manager_id = e2.employee_id
WHERE e1.salary < 30000
  AND e2.employee_id IS NULL -- means there is no id for the manager, so he has left the company
  AND e1.manager_id IS NOT NULL
ORDER BY employee_id;

-- Subquery
SELECT employee_id
FROM Employees
WHERE salary < 30000
  AND manager_id NOT IN (SELECT employee_id
                         FROM Employees)
ORDER BY employee_id;