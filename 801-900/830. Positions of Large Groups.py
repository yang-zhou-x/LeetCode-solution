'''
In a string S of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
Call a group large if it has 3 or more characters.  
We would like the starting and ending positions of every large group.
The final answer should be in lexicographic order.

Example 1:
Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

Example 2:
Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.

Example 3:
Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]

Note:  1 <= S.length <= 1000
'''

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        if len(S) < 3:
            return []
        ans = []
        anchor = 0
        for i in range(1, len(S)):
            if S[i] != S[anchor]:
                if i - anchor > 2:
                    ans.append([anchor, i - 1])
                anchor = i
        # the last one
        if len(S) - anchor > 2:
            ans.append([anchor, i])
        return ans
# Runtime: 28 ms, faster than 98.81% of Python3 online submissions for Positions of Large Groups.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Positions of Large Groups.
