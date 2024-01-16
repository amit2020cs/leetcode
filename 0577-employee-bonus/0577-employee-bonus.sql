# Write your MySQL query statement below
select name, bonus from Employee
left join Bonus Using(Empid)

where bonus< 1000 or bonus is NULL