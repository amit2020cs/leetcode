# Write your MySQL query statement below
select class
from (
select class , count(student) as num from Courses
group by class) as temp
where num >=5