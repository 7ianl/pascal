# Write your MySQL query statement below
select name as Customers
from Customers C
where id not in(
    select customerId from Orders 
)