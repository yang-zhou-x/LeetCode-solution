# Write your MySQL query statement below
select Name Customers
from Customers
where Id not in (select CustomerId
                from Orders)
                
# Runtime: 244 ms, faster than 87.89% of MySQL online submissions for Customers Who Never Order.
# Memory Usage: N/A
