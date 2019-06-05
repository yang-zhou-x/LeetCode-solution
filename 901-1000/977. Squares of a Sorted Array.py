'''
Given an array of integers A sorted in non-decreasing order, 
return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
'''

# 解法1
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = []
        posi = 0
        while posi < len(A) and A[posi] < 0:
            posi += 1
        nega = posi-1
        while nega >= 0 and posi < len(A):
            if -A[nega] < A[posi]:
                ans.append(A[nega]**2)
                nega -= 1
            else:
                ans.append(A[posi]**2)
                posi += 1
        while nega >= 0:
            ans.append(A[nega]**2)
            nega -= 1
        while posi < len(A):
            ans.append(A[posi]**2)
            posi += 1
        return ans
# Runtime: 204 ms, faster than 20.12% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 15.3 MB, less than 5.11% of Python3 online submissions for Squares of a Sorted Array.

# 解法2：实际运行更快
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = [a**2 for a in A]
        ans.sort()
        return ans
# Runtime: 172 ms, faster than 70.60% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 15.2 MB, less than 21.18% of Python3 online submissions for Squares of a Sorted Array.
