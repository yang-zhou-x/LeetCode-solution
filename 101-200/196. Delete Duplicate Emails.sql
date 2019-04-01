# Write your MySQL query statement below
delete p1
from Person p1,Person p2
where p1.Email=p2.Email and p1.Id>p2.Id

# Runtime: 738 ms, faster than 47.83% of MySQL online submissions for Delete Duplicate Emails.
# Memory Usage: N/A

# 另一种稍快的方法
delete p1
from Person p1
    join Person p2
    on p1.Email=p2.Email
where p1.Id>p2.Id

# Runtime: 697 ms, faster than 76.88% of MySQL online submissions for Delete Duplicate Emails.
# Memory Usage: N/A
