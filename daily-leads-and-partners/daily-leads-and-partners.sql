# Write your MySQL query statement below
SELECT date_id,make_name,count(distinct lead_id) AS 'Unique_Leads' ,count(distinct partner_id) AS 'Unique_Partners'
FROM DailySales
GROUP BY date_id,make_name;