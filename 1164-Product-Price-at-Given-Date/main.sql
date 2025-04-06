-- Approach 1: Divide cases by using UNION

-- note: In order to select cols that are not in GROUP BY, use a sub query with IN operator like:
-- select x, y
-- from products
-- where x in
--       (select x
--        from products
--        group by x)

with before_date as (select product_id, new_price as price
                     from products
                     where (product_id, change_date) in
                           (select product_id, max(change_date) as recent_date
                            from products
                            where change_date <= '2019-08-16'
                            group by product_id)),

     after_date as (select product_id, 10 as price
                    from products
                    group by product_id
                    having min(change_date) > '2019-08-16')

select *
from before_date
union all
select *
from after_date;

--------
-- Approach 2: Divide cases by using LEFT JOIN

--------

-- Approach 3: Use the window function
SELECT product_id,
       IFNULL(price, 10) AS price
FROM (SELECT DISTINCT product_id
      FROM Products) AS UniqueProducts
         LEFT JOIN (SELECT DISTINCT product_id,
                                    FIRST_VALUE(new_price) OVER (
                                        PARTITION BY
                                            product_id
                                        ORDER BY
                                            change_date DESC
                                        ) AS price
                    FROM Products
                    WHERE change_date <= '2019-08-16') AS LastChangedPrice USING (product_id);