# Write your MySQL query statement below
update salary
set sex=case sex
    when 'm' then 'f' else 'm'
    end;
    
# Runtime: 143 ms, faster than 85.26% of MySQL online submissions for Swap Salary.
# Memory Usage: N/A
