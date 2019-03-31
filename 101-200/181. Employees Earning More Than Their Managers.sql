# Write your MySQL query statement below
select a.Name as Employee
from Employee a
    left join Employee b
    on a.ManagerId=b.Id
where a.Salary>b.Salary

# Runtime: 300 ms, faster than 70.24% of MySQL online submissions for Employees Earning More Than Their Managers.
# Memory Usage: N/A
