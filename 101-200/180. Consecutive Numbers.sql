# Write your MySQL query statement below
select distinct l1.Num ConsecutiveNums
from Logs l1,Logs l2,Logs l3
where l1.Id=l2.Id-1
    and l2.Id=l3.Id-1
    and l1.Num=l2.Num
    and l2.num=l3.num
    
# Runtime: 364 ms, faster than 24.98% of MySQL online submissions for Consecutive Numbers.

# Write your MySQL query statement below
select distinct l1.Num ConsecutiveNums
from Logs l1
    left join Logs l2
    on l1.Id=l2.Id-1
    left join Logs l3
    on l2.Id=l3.Id-1
where l1.Num=l2.Num
    and l2.num=l3.num
    
# Runtime: 343 ms, faster than 61.70% of MySQL online submissions for Consecutive Numbers.
