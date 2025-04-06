with min_year_table as (select product_id, min(year) min_year
                        from sales
                        group by product_id)

select s.product_id, s.year first_year, quantity, price
from sales s
         inner join min_year_table m on s.product_id = m.product_id and s.year = m.min_year