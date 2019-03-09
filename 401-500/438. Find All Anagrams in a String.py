class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or len(s)<len(p):
            return []
        ans=[]
        p_count=collections.Counter(p)
        len_p=len(p)
        window=collections.Counter(s[:len_p])
        if p_count==window:
            ans.append(0)
        for i in range(len_p,len(s)):  # i是窗口结束的位置
            window[s[i-len_p]]-=1
            if window[s[i-len_p]]==0:  # 等于0时移出，避免影响判断
                window.pop(s[i-len_p])
            window[s[i]]+=1
            if window==p_count:
                ans.append(i-len_p+1)
        return ans
        
# Runtime: 192 ms, faster than 47.59% of Python online submissions for Find All Anagrams in a String.
# Memory Usage: 12.1 MB, less than 32.26% of Python online submissions for Find All Anagrams in a String.

# 更快的方法，仅限Python3：
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or len(s)<len(p):
            return []
        ans=[]
        hs,hp=0,0
        for i in range(len(p)):
            hs+=hash(s[i])
            hp+=hash(p[i])
        if hs==hp:
            ans.append(0)
        for right in range(len(p),len(s)):  # right是窗口结束的位置
            left=right-len(p)
            hs+=hash(s[right])-hash(s[left])
            if hs==hp:
                ans.append(left+1)
        return ans
        
# Runtime: 100 ms, faster than 97.07% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 14.1 MB, less than 5.19% of Python3 online submissions for Find All Anagrams in a String.
