# Write your MySQL query statement below
select s1.id, coalesce(s2.student,s1.student) student
from seat s1
    left join seat s2
    on ((s1.id+1)^1)-1=s2.id # 按位操作符
order by s1.id

# Runtime: 177 ms, faster than 60.58% of MySQL online submissions for Exchange Seats.
# Memory Usage: N/A
