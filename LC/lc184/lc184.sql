# Write your MySQL query statement below
with A as (
    select max(salary) as Salary, departmentId
    from Employee
    group by departmentId
)
select C.name as Department, A.Salary, B.name as Employee 
from A, Employee B, Department C
where A.departmentId = B.departmentId
and A.Salary = B.salary
and B.departmentId = C.id