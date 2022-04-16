# Write your MySQL query statement below
SELECT email
FROM Person
GROUP BY email
HAVING count(*) > 1 
# SELECT * 
# FROM Person 
# WHERE Color IN (
#   SELECT email  
#   FROM StyleTable   
#   GROUP BY Color  
#   HAVING count(*) > 1 
# ) 