class Solution:
    def reverse(self, x: 'int') -> 'int':
        if x>0:
            sign=1
        else:
            sign=-1
            x=-x
            
        ans=0
        while x>0:
            ans=ans*10+x%10
            x=x//10
        
        return sign*ans if ans<2147483648 and ans>-2147483649 else 0
        
# Runtime: 48 ms, faster than 99.90% of Python3 online submissions for Reverse Integer.
# Memory Usage: 12.5 MB, less than 66.75% of Python3 online submissions for Reverse Integer.
