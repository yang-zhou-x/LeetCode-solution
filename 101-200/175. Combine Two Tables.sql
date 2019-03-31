# Write your MySQL query statement below
select FirstName, LastName, City, State
from Person p
    left join Address a
    on p.PersonId = a.PersonId
    
# Runtime: 213 ms, faster than 76.26% of MySQL online submissions for Combine Two Tables.
# Memory Usage: N/A
