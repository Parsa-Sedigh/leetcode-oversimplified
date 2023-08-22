SELECT w2.id AS Id
FROM Weather w1
         INNER JOIN Weather w2 ON w2.temperature > w1.temperature
WHERE w2.temperature > w1.temperature
  AND DATEDIFF(w2.recordDate, w1.recordDate) = 1;