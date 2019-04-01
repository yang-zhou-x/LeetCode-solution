# Write your MySQL query statement below
select (select distinct Salary
        from Employee
        order by Salary desc
        limit 1 offset 1) SecondHighestSalary
        
# Runtime: 130 ms, faster than 77.44% of MySQL online submissions for Second Highest Salary.
# Memory Usage: N/A
