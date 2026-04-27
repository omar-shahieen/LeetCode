# Write your MySQL query statement below
-- name, population, and area
-- big countries.
-- it has an area of at least three million (i.e., 3000000 km2), or
-- it has a population of at least twenty-five million (i.e., 25000000).

select name , population , area
from world 
where area >= 3000000 or population >=25000000