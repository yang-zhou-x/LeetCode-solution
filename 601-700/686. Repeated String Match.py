'''
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. 
If no such solution, return -1.

For example, 
with A = "abcd" and B = "cdabcdab".
Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; 
and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
'''

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        repeat = 1
        tmp = A
        maxi_rep = 1
        while maxi_rep * len(A) + 1 < len(B):
            maxi_rep += 1
        while maxi_rep >= 0:
            if tmp.find(B) < 0:
                tmp += A
                repeat += 1
                maxi_rep -= 1
            else:
                return repeat
        return -1
# Runtime: 112 ms, faster than 74.73% of Python3 online submissions for Repeated String Match.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Repeated String Match.
