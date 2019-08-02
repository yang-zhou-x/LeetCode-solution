'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
Below is one possible representation of s1 = "great":
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.
For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".
Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:
Input: s1 = "great", s2 = "rgeat"
Output: true

Example 2:
Input: s1 = "abcde", s2 = "caebd"
Output: false
'''

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if Counter(s1) != Counter(s2):
            return False
        if s1 == s2:
            return True
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[i:], s2[:-i]) and self.isScramble(s1[:i], s2[-i:]):
                return True
        return False
# Runtime: 84 ms, faster than 25.53% of Python3 online submissions for Scramble String.
# Memory Usage: 13.6 MB, less than 6.12% of Python3 online submissions for Scramble String.

# use cache
from collections import Counter

class Solution:
    def __init__(self):
        self.cache = {}
        
    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.cache:
            return self.cache[s1, s2]
        if Counter(s1) != Counter(s2):
            self.cache[s1,s2] = False
            return False
        if s1 == s2:
            self.cache[s1,s2] = True
            return True
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
                self.isScramble(s1[i:], s2[:-i]) and self.isScramble(s1[:i], s2[-i:]):
                return True
        self.cache[s1,s2] = False
        return False
# Runtime: 72 ms, faster than 32.98% of Python3 online submissions for Scramble String.
# Memory Usage: 13.8 MB, less than 6.12% of Python3 online submissions for Scramble String.
