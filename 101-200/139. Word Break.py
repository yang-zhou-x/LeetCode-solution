'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*len(s)  # 用于记录结果
        for idx in range(len(s)):
            # idx作为结束位置，比较此之前的字符串
            for word in wordDict:
                # 当该段字符串与某一个word匹配，并且word是第1个匹配字段或者此前相邻的一段字符串匹配时
                if word == s[idx-len(word)+1:idx+1] and (idx-len(word) == -1 or dp[idx-len(word)]):
                    dp[idx] = True
                    break
        return dp[-1]
        
# Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Word Break.
# Memory Usage: 12.9 MB, less than 8.24% of Python3 online submissions for Word Break.
