class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        aux={')':'(','}':'{',']':'['}
        for ss in s:
            if ss=='('or ss=='[' or ss=='{':
                stack.append(ss)
            else:
                try:
                    x=stack.pop()
                except:
                    return False
                if x!=aux[ss]:
                    return False
        return len(stack)==0
                
# Runtime: 20 ms, faster than 96.20% of Python online submissions for Valid Parentheses.
# Memory Usage: 10.8 MB, less than 41.31% of Python online submissions for Valid Parentheses.
