SELECT "Low Salary"        AS category,
       sum(income < 20000) AS accounts_count
FROM Accounts

UNION

SELECT "Average Salary"                    AS category,
       sum(income BETWEEN 20000 AND 50000) AS accounts_count
FROM Accounts

UNION

SELECT "High Salary"       AS category,
       sum(income > 50000) AS accounts_count
FROM Accounts;

---------------

-- approach 2:
SELECT unnest(array ['Low Salary', 'Average Salary', 'High Salary']) AS "category",
       unnest(array [
           SUM(CASE WHEN income < 20000 THEN 1 ELSE 0 END),
           SUM(CASE WHEN income BETWEEN 20000 AND 50000 THEN 1 ELSE 0 END),
           SUM(CASE WHEN income > 50000 THEN 1 ELSE 0 END)
           ])                                                        AS "accounts_count"
FROM Accounts;