# Write your MySQL query statement below
-- name and bonus amount of each employee
-- The employee has a bonus less than 1000.
-- The employee did not get any bonus.
select e.name , b.bonus  
from employee e
left join bonus b
on e.empId = b.empId 
where b.bonus < 1000 or b.bonus is NULL
