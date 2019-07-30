'''
Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), 
the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:
Input: "1 + 1"
Output: 2

Example 2:
Input: " 2-1 + 2 "
Output: 3

Example 3:
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0
        sign = 1  # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            elif ch == '+':
                res += sign * operand
                sign = 1  # 下一轮使用
                operand = 0
            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == '(':
                # Push the result and sign on to the stack, for later
                stack.append(res)
                stack.append(sign)
                # Reset operand and result
                sign = 1
                res = 0
            elif ch == ')':
                res += sign * operand
                res *= stack.pop()  # sign
                res += stack.pop()  # operand
                operand = 0
        return res + sign * operand
# Runtime: 120 ms, faster than 56.44% of Python3 online submissions for Basic Calculator.
# Memory Usage: 15.6 MB, less than 19.05% of Python3 online submissions for Basic Calculator.
