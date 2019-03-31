class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0 # Substring的起始位置
        ans=0
        cache={}  # 用来记录每个字母最近一次出现的位置
        for i,ss in enumerate(s):
            if ss in cache and start<=cache[ss]:
                start=cache[ss]+1
                cache[ss]=i # 更新位置
            else:
                ans=max(ans,i-start+1)
                cache[ss]=i # 添加位置
        return ans
        
# Runtime: 44 ms, faster than 99.14% of Python online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 11.2 MB, less than 49.60% of Python online submissions for Longest Substring Without Repeating Characters.
