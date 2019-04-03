# Write your MySQL query statement below
select d.Name Department, e.Name Employee, e.Salary
from Employee e
    join Department d
    on e.DepartmentId=d.Id
where (e.DepartmentId,e.Salary) in (select DepartmentId,max(Salary)
                                    from Employee
                                    group by DepartmentId)
                  
# Runtime: 330 ms, faster than 52.86% of MySQL online submissions for Department Highest Salary.
