-- we need every user to be in the output. But some of them are not in confirmations table. So we need to use:
-- `from signups left join confirmations`

select user_id,
       round(
               sum(case when action = 'confirmed' then 1 else 0 end)::decimal
                   /

                   -- we need to count(*) on the table derived from JOIN and GROUP BY, not the whole confirmations
               (count(*)), 2) as confirmation_rate
from signups
         left join confirmations using (user_id)
group by (user_id)