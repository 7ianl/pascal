# Write your MySQL query statement below
delete a from Person a, Person b
where a.id > b.id and a.email = b.email