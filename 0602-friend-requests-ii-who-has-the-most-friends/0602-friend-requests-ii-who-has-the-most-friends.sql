# Write your MySQL query statement below
with cte_1 as (
    select requester_id as id,count(requester_id) as count_
    from RequestAccepted
    group by requester_id

    UNION ALL

    select accepter_id as id,count(accepter_id) as count_
    from RequestAccepted
    group by accepter_id),

cte_2 as(
    select id,sum(count_) as num
    from cte_1
    group by id)

select id,num
from cte_2
order by num desc
limit 1;