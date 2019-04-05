CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare m int;
set m=N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct Salary
      from Employee
      order by Salary desc
      limit m,1
  );
END
# Runtime: 189 ms, faster than 57.48% of MySQL online submissions for Nth Highest Salary.

# 另一种写法：
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set N=N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct Salary
      from Employee
      order by Salary desc
      limit 1 offset N
  );
END
# Runtime: 186 ms, faster than 67.11% of MySQL online submissions for Nth Highest Salary.
