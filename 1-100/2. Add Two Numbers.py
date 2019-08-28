'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = 0  # 记录进位
        p = dummy
        while l1 or l2 or curr:
            if l1:
                curr += l1.val
                l1 = l1.next
            if l2:
                curr += l2.val
                l2 = l2.next
            p.next = ListNode(curr % 10)
            p = p.next
            curr //= 10
        return dummy.next
# Runtime: 72 ms, faster than 96.04% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13 MB, less than 96.64% of Python3 online submissions for Add Two Numbers.
