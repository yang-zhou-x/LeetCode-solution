# Write your MySQL query statement below
select b.Name Department, a.Name Employee, a.Salary
from Employee a
    join Department b
    on a.DepartmentId = b.Id
where (select count(distinct a2.Salary)
      from Employee a2
      where a2.Salary>a.Salary
        and a2.DepartmentId=a.DepartmentId) < 3
        
# Runtime: 722 ms, faster than 41.46% of MySQL online submissions for Department Top Three Salaries.
