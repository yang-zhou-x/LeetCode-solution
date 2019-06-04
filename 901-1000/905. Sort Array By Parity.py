'''
Given an array A of non-negative integers, 
return an array consisting of all the even elements of A, 
followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 
Note:
1 <= A.length <= 5000
0 <= A[i] <= 5000
'''

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for a in A:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)
        return even+odd
# Runtime: 60 ms, faster than 98.81% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 13.9 MB, less than 10.15% of Python3 online submissions for Sort Array By Parity.
