# Write your MySQL query statement below
select 'Low Salary' as category,
        sum(case when income < 20000 then 1 else 0 end) as accounts_count
from Accounts
union

SELECT  
    'Average Salary' category,
    SUM(CASE WHEN income >= 20000 AND income <= 50000 THEN 1 ELSE 0 END) 
    AS accounts_count
FROM 
   Accounts

UNION
SELECT 
    'High Salary' category,
    SUM(CASE WHEN income > 50000 THEN 1 ELSE 0 END) AS accounts_count
FROM 
    Accounts
order by accounts_count desc