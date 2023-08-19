SELECT Employee.name, Bonus.bonus
FROM Employee
         LEFT JOIN Bonus USING (empId)
WHERE Bonus.bonus < 1000
   OR Bonus.bonus IS NULL;
