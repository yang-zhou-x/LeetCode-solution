'''
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        def is_palindrome(s):
            return s == s[::-1]
        
        def back_track(remain, path):
            if not remain:
                ans.append(path)  # path储存了所有回文片段
            else:
                for i in range(1, len(remain) + 1):
                    if is_palindrome(remain[:i]):
                        back_track(remain[i:], path + [remain[:i]])
        back_track(s, [])
        return ans
# Runtime: 88 ms, faster than 76.44% of Python3 online submissions for Palindrome Partitioning.
# Memory Usage: 14 MB, less than 5.88% of Python3 online submissions for Palindrome Partitioning.
