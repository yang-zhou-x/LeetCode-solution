# Write your MySQL query statement below
select w2.Id
from Weather w1
    left join Weather w2
    on datediff(w2.RecordDate,w1.RecordDate)=1
where w2.Temperature>w1.Temperature

# Runtime: 307 ms, faster than 94.86% of MySQL online submissions for Rising Temperature.
# Memory Usage: N/A
