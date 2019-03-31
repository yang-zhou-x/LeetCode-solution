# Write your MySQL query statement below
select id,movie,description,rating
from cinema
where id % 2=1 and description != 'boring'
order by rating desc

# Runtime: 140 ms, faster than 43.28% of MySQL online submissions for Not Boring Movies.
# Memory Usage: N/A
