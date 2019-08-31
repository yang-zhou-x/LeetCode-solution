'''
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
 
Example 1:
Input: "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: "III"
Output: [0,1,2,3]

Example 3:
Input: "DDI"
Output: [3,2,0,1]

Note:
1 <= S.length <= 10000
S only contains characters "I" or "D".
''

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        left, right = 0, len(S)
        ans = [0] * (len(S) + 1)
        for i, cha in enumerate(S):
            if cha == 'I':
                ans[i] = left
                left += 1
            else:
                ans[i] = right
                right -=1
        ans[-1] = left
        return ans
# Runtime: 76 ms, faster than 71.95% of Python3 online submissions for DI String Match.
# Memory Usage: 15 MB, less than 5.00% of Python3 online submissions for DI String Match.
        
