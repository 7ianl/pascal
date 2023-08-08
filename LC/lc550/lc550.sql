# Write your MySQL query statement below
with t1 as (
    select player_id, min(event_date) as event_date from Activity
    group by player_id
), t2 as (
    select count(*) as ret
    from t1, Activity a
    where t1.player_id = a.player_id
    and datediff(a.event_date, t1.event_date) =1
)
select round(ret/count(t1.player_id), 2) as fraction from t1, t2