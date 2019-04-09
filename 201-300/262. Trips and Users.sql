# Write your MySQL query statement below
select Request_at Day,
        round(sum(case when lower(Status) like 'cancelled%' then 1 else 0 end)/count(*),2) 'Cancellation Rate'
from trips t
    join users u
    on t.Client_Id = u.Users_Id
where (Request_at between '2013-10-01' and '2013-10-03')
    and u.Banned='No'
group by Request_at

# Runtime: 198 ms, faster than 89.13% of MySQL online submissions for Trips and Users.
