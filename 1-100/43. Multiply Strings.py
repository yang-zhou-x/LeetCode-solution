'''
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = [0] * (len(num1) + len(num2))  # 乘积最长是这么多位数
        pos = len(product) - 1
        # 和手动计算乘法的步骤一样
        for n1 in reversed(num1):
            tmpPos = pos
            for n2 in reversed(num2):
                product[tmpPos] += int(n1) * int(n2)
                product[tmpPos - 1] += product[tmpPos] // 10  # 进位
                product[tmpPos] %= 10
                tmpPos -= 1  # 下一个数字
            pos -= 1  # 末位提前1个
        left = 0
        while left < len(product) - 1 and product[left] == 0:
            left += 1
        return ''.join(map(str, product[left:]))
# Runtime: 152 ms, faster than 42.40% of Python3 online submissions for Multiply Strings.
# Memory Usage: 13.5 MB, less than 7.14% of Python3 online submissions for Multiply Strings.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
# Runtime: 32 ms, faster than 98.17% of Python3 online submissions for Multiply Strings.
# Memory Usage: 13.6 MB, less than 5.46% of Python3 online submissions for Multiply Strings.
