with first_login_date as (select player_id, min(event_date) as first_login
                          from activity
                          group by player_id),
     player_at_next_day as (select *
                            from activity a
                                     inner join first_login_date f on a.player_id = f.player_id
                            where a.event_date = f.first_login + 1),
     total_players as (select count(distinct player_id)
                       from activity)

select round(
                   (select count(*) from player_at_next_day)::decimal
                   /
                   (select * from total_players)
           , 2) as fraction;