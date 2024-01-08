# Write your MySQL query statement below
select firstname,lastname , City,State from Person 
left join Address using(personId)