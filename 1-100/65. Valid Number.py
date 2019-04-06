class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False
            
# Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Valid Number.
# Memory Usage: 13.4 MB, less than 5.71% of Python3 online submissions for Valid Number.
