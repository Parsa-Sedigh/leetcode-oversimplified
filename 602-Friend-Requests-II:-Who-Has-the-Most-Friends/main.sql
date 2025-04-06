with all_friends as (select requester_id as id
                     from RequestAccepted

                     union all

                     select accepter_id
                     from RequestAccepted)

select id, count(*) as num
from all_friends
group by id
order by num desc
limit 1;