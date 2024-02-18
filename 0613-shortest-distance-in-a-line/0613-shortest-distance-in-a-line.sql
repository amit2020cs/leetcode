# Write your MySQL query statement below
select  min(p1.x - p2.x) shortest 

from Point p1
inner join Point p2 on p1.x > p2.x
