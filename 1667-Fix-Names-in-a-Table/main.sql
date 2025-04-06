-- make the first letter uppercase, so the start_index is 1 and length(second param of substr) is also 1.
-- then make the rest lowercase, so start_index is 2 and length is char_length(name) which means until the end.

select user_id,
       concat(upper(substr(name, 1, 1)), lower(substr(name, 2, char_length(name)))) as name
from users
order by user_id