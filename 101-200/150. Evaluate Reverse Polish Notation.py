'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:
Division between two integers should truncate toward zero.
The given RPN expression is always valid. 
That means the expression would always evaluate to a result and there won't be any divide by zero operation.

Example 1:
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in '+-*/':
                stack.append(int(t))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if t == '+':
                    tmp = operand1 + operand2
                elif t == '-':
                    tmp = operand1 - operand2
                elif t == '*':
                    tmp = operand1 * operand2
                else:
                    tmp = int(operand1 / operand2)
                stack.append(tmp)
        return stack[0]
# Runtime: 76 ms, faster than 83.95% of Python3 online submissions for Evaluate Reverse Polish Notation.
# Memory Usage: 14.1 MB, less than 5.10% of Python3 online submissions for Evaluate Reverse Polish Notation.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {'+', '-', '*', '/'}
        for t in tokens:
            if t not in operator:
                stack.append(int(t))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if t == '+':
                    tmp = operand1 + operand2
                elif t == '-':
                    tmp = operand1 - operand2
                elif t == '*':
                    tmp = operand1 * operand2
                else:
                    tmp = int(operand1 / operand2)
                stack.append(tmp)
        return stack[0]
# Runtime: 76 ms, faster than 83.95% of Python3 online submissions for Evaluate Reverse Polish Notation.
# Memory Usage: 13.9 MB, less than 5.10% of Python3 online submissions for Evaluate Reverse Polish Notation.
