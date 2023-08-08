# Write your MySQL query statement below
select b.name as Department, a.name as Employee, a.salary as Salary
from Employee a, Department b
where a.departmentId = b.id
and 3 > (select count(distinct a2.salary) from Employee a2
        where a.salary < a2.salary and a.departmentId = a2.departmentId)