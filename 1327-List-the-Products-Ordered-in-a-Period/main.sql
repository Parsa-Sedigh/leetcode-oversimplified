select product_name, sum(unit) as unit
from (select *
      from orders
      where TO_CHAR(order_date, 'YYYY-MM') = '2020-02') as o
         inner join Products p
                    on o.product_id = p.product_id
group by o.product_id, product_name
having sum(unit) >= 100