'''
You are given a string, s, and a list of words, words, 
that are all of the same length. Find all starting indices of substring(s) 
in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        ans = []
        for i in range(len(s) - len(words[0]) * len(words) + 1):
            remain = words.copy()
            for j in range(len(words)):
                check = s[i + j * len(words[0]): i + (j + 1) * len(words[0])]
                if check in remain:
                    remain.remove(check)
                else:
                    break
            if not remain:
                ans.append(i)
        return ans
# Runtime: 1456 ms, faster than 7.26% of Python3 online submissions for Substring with Concatenation of All Words.
# Memory Usage: 13.8 MB, less than 6.50% of Python3 online submissions for Substring with Concatenation of All Words.

# 改进一点
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        from collections import Counter
        ans = []
        w_len = len(words[0])
        n_words = len(words)
        check = Counter(words)
        for i in range(len(s) - w_len * n_words + 1):
            window = [s[i + k * w_len: i + (k + 1) * w_len] for k in range(n_words)]
            if Counter(window) == check:
                ans.append(i)
        return ans
# Runtime: 1012 ms, faster than 18.65% of Python3 online submissions for Substring with Concatenation of All Words.
# Memory Usage: 14.1 MB, less than 5.69% of Python3 online submissions for Substring with Concatenation of All Words.

# 换了思路
class Solution:  # 56 ms
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or words == []:
            return []
        lenstr = len(s)
        lenword = len(words[0])
        lensubstr = len(words)*lenword
        times = {}
        for word in words:
            if word in times:
                times[word] += 1
            else:
                times[word] = 1
        ans = []
        for i in range(min(lenword, lenstr - lensubstr + 1)):
            self.findAnswer(i, lenstr, lenword, lensubstr, s, times, ans)
        return ans

    def findAnswer(self, strstart, lenstr, lenword, lensubstr, s, times, ans):
        wordstart = strstart
        curr = {}
        while strstart + lensubstr <= lenstr:
            word = s[wordstart: wordstart + lenword]
            wordstart += lenword
            if word not in times:
                strstart = wordstart
                curr.clear()
            else:
                if word in curr:
                    curr[word] += 1
                else:
                    curr[word] = 1
                while curr[word] > times[word]:
                    curr[s[strstart: strstart + lenword]] -= 1
                    strstart += lenword
                if wordstart - strstart == lensubstr:
                    ans.append(strstart)
# Runtime: 56 ms, faster than 100.00% of Python3 online submissions for Substring with Concatenation of All Words.
# Memory Usage: 14.1 MB, less than 5.69% of Python3 online submissions for Substring with Concatenation of All Words.
