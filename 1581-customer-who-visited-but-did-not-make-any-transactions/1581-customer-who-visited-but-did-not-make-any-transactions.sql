# Write your MySQL query statement below
--  IDs of the users who visited without making any transactions 
--  the number of times they made these types of visits.
select v.customer_id , count(*) as count_no_trans
from visits v
left join transactions t 
on t.visit_id  = v.visit_id 
where t.visit_id is NULL
group by v.customer_id 