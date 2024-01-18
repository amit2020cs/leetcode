# Write your MySQL query statement below
select contest_id, ROUND((count(r.user_id)* 100) / (SELECT COUNT(DISTINCT user_id) FROM Users), 2 ) as percentage
from Users u 
join Register r on r.user_id = u.user_id
GROUP BY contest_id
ORDER BY percentage DESC, contest_id asc;
