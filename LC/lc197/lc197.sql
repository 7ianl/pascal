# Write your MySQL query statement below
with a as (select id, temperature, DATE_ADD(recordDate, interval 1 day) as nextDay from Weather)
select b.id from a, Weather b
where nextDay = b.recordDate
and a.temperature < b.temperature