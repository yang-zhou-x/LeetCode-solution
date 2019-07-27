'''
Write a function that reverses a string. 
The input string is given as an array of characters char[].
Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()
        
# 20190727
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        if n % 2 == 0:
            left = n >> 1
        else:
            left = (n + 1) >> 1
        for i in range(left):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
# Runtime: 248 ms, faster than 18.37% of Python3 online submissions for Reverse String.
# Memory Usage: 17.7 MB, less than 34.05% of Python3 online submissions for Reverse String.
