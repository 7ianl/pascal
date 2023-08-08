# Write your MySQL query statement below
select name from SalesPerson where sales_id not in
(select sales_id from Company c, Orders o 
 where c.com_id = o.com_id and name = "RED")