'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; 
otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1 = collections.Counter(ransomNote)
        cnt2 = collections.Counter(magazine)
        for key in cnt1:
            if cnt1[key] > cnt2[key]:
                return False
        return True
# Runtime: 68 ms, faster than 44.09% of Python3 online submissions for Ransom Note.
# Memory Usage: 13.8 MB, less than 5.59% of Python3 online submissions for Ransom Note.
