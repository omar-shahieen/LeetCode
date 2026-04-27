# Write your MySQL query statement below
-- required
-- the average time each machine takes to complete a process.
-- eq
-- The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.
-- return 
-- The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.

select a1.machine_id  as machine_id  , ROUND(AVG((a2.timestamp - a1.timestamp) ),3 ) as processing_time
from activity a1
join activity a2 
on  a1.machine_id = a2.machine_id and a1.process_id  = a2.process_id 
where  a1.activity_type  like 'start' and a2.activity_type like 'end' 
group by a1.machine_id
   

