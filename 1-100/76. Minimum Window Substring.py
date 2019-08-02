'''
Given a string S and a string T, find the minimum window in S 
which will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        dict_t = collections.Counter(t)
        required = len(dict_t)  # t中不同字母的数量
        left, right = 0, 0  # two pointer
        formed = 0  # 当前窗口中满足条件的不同字母的数量
        window_cnt = {}  # 窗口，并对不同字母计数
        ans = float('inf'), None, None  # window length, left, right
        while right < len(s):  # expand the window
            ch = s[right]
            window_cnt[ch] = window_cnt.get(ch, 0) + 1
            if ch in dict_t and window_cnt[ch] == dict_t[ch]:
                formed += 1
            while left <= right and formed == required:  # contract the window
                ch = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                window_cnt[ch] -= 1
                if ch in dict_t and window_cnt[ch] < dict_t[ch]:
                    formed -= 1
                left += 1
            right += 1
        return '' if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]
# Runtime: 132 ms, faster than 66.47% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 14.6 MB, less than 7.72% of Python3 online submissions for Minimum Window Substring.
