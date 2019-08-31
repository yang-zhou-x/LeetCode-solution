'''
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cache=set()
        while n!=1:
            if n in cache:
                return False
            cache.add(n)
            n=sum(int(x)**2 for x in str(n))
        return True
# Runtime: 24 ms, faster than 91.81% of Python online submissions for Happy Number.
# Memory Usage: 10.8 MB, less than 27.56% of Python online submissions for Happy Number.
 
# 20190831 review
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            n = sum(int(x) ** 2 for x in str(n))
        return True
# Runtime: 40 ms, faster than 74.55% of Python3 online submissions for Happy Number.
# Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Happy Number.
