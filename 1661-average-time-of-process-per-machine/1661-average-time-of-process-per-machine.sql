# Write your MySQL query statement below
select machine_id,

ROUND(SUM(
CASE WHEN activity_type='start' THEN timestamp*-1 ELSE timestamp END) *1.0
      / (select count(distinct process_id)),3) as processing_time
      from Activity
GROUP BY machine_id