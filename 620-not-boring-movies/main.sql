-- my approach
SELECT id, movie, description, rating
FROM cinema
WHERE id % 2 = 1
  AND description NOT LIKE '%boring%'
ORDER BY rating DESC;