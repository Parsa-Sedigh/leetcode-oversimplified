(select name as results
 from movieRating
          inner join users using (user_id)
 group by name
 order by count(*) desc, name
 limit 1)

union all

(select title
 from movieRating
          inner join movies using (movie_id)
 where to_char(created_at, 'yyyy-mm') = '2020-02'
 group by title
 order by avg(rating) desc, title
 limit 1)