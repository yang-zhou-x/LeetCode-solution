class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans=[]
        idx=0
        while idx<len(A) and A[idx]<0:
            idx+=1
        left=idx-1
        while left>=0 and idx<len(A):
            if A[left]**2<A[idx]**2:
                ans.append(A[left]**2)
                left-=1
            else:
                ans.append(A[idx]**2)
                idx+=1
                
        while left>=0:
            ans.append(A[left]**2)
            left-=1
            
        while idx<len(A):
            ans.append(A[idx]**2)
            idx+=1
        
        return ans

# 另一个答案，实际运行更快
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans=[x**2 for x in A]
        ans.sort()
        return ans
        
