'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        ans=strs[0]
        for s in strs[1:]:
            while not s.startswith(ans) and len(ans)>0:
                ans=ans[:-1]
        return ans
# Runtime: 16 ms, faster than 100.00% of Python online submissions for Longest Common Prefix.
# Memory Usage: 11.2 MB, less than 5.66% of Python online submissions for Longest Common Prefix.

# 2019/7/23
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        ans = strs[0]
        for s in strs[1:]:
            # 每一个单词都要以prefix开头。不满足则去掉末尾1个字母。
            while not s.startswith(ans) and len(ans) > 0:
                ans = ans[:-1]
        return ans
# Runtime: 40 ms, faster than 49.81% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14 MB, less than 5.30% of Python3 online submissions for Longest Common Prefix.
