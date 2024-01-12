# Write your MySQL query statement below
select a.sale_date, a.sold_num - b.sold_num as diff

from sales a, sales b

where a.fruit in ("apples") and b.fruit in ('oranges')

and a.sale_date = b.sale_date

group by 1
order by 1