-- note: It's important to have () around the SELECT in the HAVING here.

SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(distinct product_key) = (SELECT COUNT(product_key) FROM Product)