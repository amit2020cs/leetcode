# Write your MySQL query statement below
SELECT employee_id, COUNT(*)
over (PARTITION BY team_id) AS team_size
FROM employee