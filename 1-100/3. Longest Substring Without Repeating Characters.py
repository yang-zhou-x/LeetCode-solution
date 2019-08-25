'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# 2019/07/22
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        pos = {}  # 用来记录每个字母最近一次出现的位置
        start = 0
        ans = 0
        for i, ss in enumerate(s):
            # pos中是所有字母的位置。字串中可能不包含所有字母。
            # start <= pos[ss] 确保该重复字母出现在当前字串中
            if ss in pos and start <= pos[ss]:
                ans = max(ans, i - start)
                start = pos[ss] + 1  # 更新起始位置
                pos[ss] = i  # 更新ss的位置
            else:
                pos[ss] = i  # 添加位置
        return max(ans, i - start + 1)
# Runtime: 52 ms, faster than 97.99% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 13.9 MB, less than 5.03% of Python3 online submissions for Longest Substring Without Repeating Characters.
