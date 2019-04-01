# Write your MySQL query statement below
select Score,(select count(*)
             from (select distinct Score s
                  from Scores) tmp
             where s>=Score) Rank
from Scores
order by Score desc

# Runtime: 204 ms, faster than 79.88% of MySQL online submissions for Rank Scores.
# Memory Usage: N/A
