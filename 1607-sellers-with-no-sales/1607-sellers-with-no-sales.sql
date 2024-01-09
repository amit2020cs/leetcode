# Write your MySQL query statement below
select seller_name
from Seller s
where s.seller_id not in (select distinct seller_id
                          from orders
                          where
                          year(sale_date)=2020)
order by 1 asc