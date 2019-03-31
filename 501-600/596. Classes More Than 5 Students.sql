# Write your MySQL query statement below
select class
from courses
group by class
having count(distinct student)>4

# Runtime: 184 ms, faster than 91.27% of MySQL online submissions for Classes More Than 5 Students.
# Memory Usage: N/A
