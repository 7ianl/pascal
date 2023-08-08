# Write your MySQL query statement below
select id, "Root" as type from Tree where p_id is null
union all (select a.id, "Inner" as type from Tree a, Tree b
where b.p_id = a.id and a.p_id is not null)
union (select id, "Leaf" as type from Tree
where id not in (select p_id from Tree where p_id is not null) and p_id is not null)
order by id