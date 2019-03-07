class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left=0
        right=len(S)
        ans=[]
        for s in S:
            if s=='I':
                ans.append(left)
                left+=1
            else:
                ans.append(right)
                right-=1
        ans.append(left)
        return ans
        
