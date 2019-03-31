# Write your MySQL query statement below
select Email
from Person
group by Email
having count(Email)>1

# Runtime: 188 ms, faster than 78.61% of MySQL online submissions for Duplicate Emails.
# Memory Usage: N/A
