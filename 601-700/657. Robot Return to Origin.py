class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('U')==moves.count('D') and moves.count('L')==moves.count('R')

# 另一种方法，实际运行较慢，时间复杂度O(n)
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        aux=collections.Counter(moves)
        return aux['U']==aux['D'] and aux['L']==aux['R']
        
