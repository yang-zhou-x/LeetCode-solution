class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1]+=1
        if digits[-1]<10:
            return digits
        next_=0
        for i in range(len(digits)-1,-1,-1):
            next_,digits[i]=divmod(digits[i]+next_,10)
        if next_!=0:
            digits.insert(0,1)
        return digits
           
# Runtime: 20 ms, faster than 97.80% of Python online submissions for Plus One.
# Memory Usage: 10.8 MB, less than 18.79% of Python online submissions for Plus One.

# 另一种思路
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        right=len(digits)-1
        while digits[right]==9:
            digits[right]=0
            right-=1
        if right<0:  # 全部为9时
            digits.insert(0,1)
            return digits
        digits[right]+=1  # 进位+1，或者直接+1
        return digits
            
# Runtime: 20 ms, faster than 97.80% of Python online submissions for Plus One.
# Memory Usage: 10.8 MB, less than 40.48% of Python online submissions for Plus One.
