class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        def f(s='',l=0,r=0):
            if len(s)==n*2:
                ans.append(s)
                return
            if l<n:
                f(s+'(',l+1,r)
            if r<l:
                f(s+')',l,r+1)
        f()
        
        return ans 
        
# Runtime: 36 ms, faster than 99.65% of Python3 online submissions for Generate Parentheses.
