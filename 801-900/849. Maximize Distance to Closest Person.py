'''
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
There is at least one empty seat, and at least one person sitting.
Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:
Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:
Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

Note:
1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
'''

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        try:
            first_idx = seats.index(1)
            last_idx = len(seats) - 1 - list(reversed(seats)).index(1)
        except ValueError:
            return len(seats)
        dp_left = [0] * (last_idx - first_idx + 1)
        dp_right = [0] * (last_idx - first_idx + 1)
        for idx in range(first_idx, last_idx + 1):
            if seats[idx] == 1:
                dp_left[idx - first_idx] = 0
            else:
                dp_left[idx - first_idx] = dp_left[idx - first_idx - 1] + 1
        for idx in reversed(range(first_idx, last_idx + 1)):
            if seats[idx] == 1:
                dp_right[idx - first_idx] = 0
            else:
                dp_right[idx - first_idx] = dp_right[idx - first_idx + 1] + 1
        tmp = max(min(x, y) for x, y in zip(dp_left, dp_right))
        return max(tmp, first_idx, len(seats) - last_idx - 1)
# Runtime: 168 ms, faster than 17.81% of Python3 online submissions for Maximize Distance to Closest Person.
# Memory Usage: 14.2 MB, less than 8.33% of Python3 online submissions for Maximize Distance to Closest Person.


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        occupied = [idx for idx in range(len(seats)) if seats[idx]]
        if len(occupied) > 1:
            interval = [occupied[idx + 1] - occupied[idx]
                        for idx in range(len(occupied) - 1)]
        else:
            interval = [0]
        return max(max(interval)//2, occupied[0], len(seats) - occupied[-1] - 1)
# Runtime: 136 ms, faster than 76.27% of Python3 online submissions for Maximize Distance to Closest Person.
# Memory Usage: 14.7 MB, less than 8.33% of Python3 online submissions for Maximize Distance to Closest Person.
