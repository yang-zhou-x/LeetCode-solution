'''
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nums1, nums2 = [0], [0]
        while l1:
            nums1.append(l1.val)
            l1 = l1.next
        while l2:
            nums2.append(l2.val)
            l2 = l2.next
        flag = 0
        right = 1
        if len(nums1) > len(nums2):
            long, short = nums1, nums2
        else:
            long, short = nums2, nums1
        while right < len(short):
            flag, long[-right] = divmod(long[-right]+short[-right]+flag, 10)
            right += 1
        while flag and right < len(long):
            flag, long[-right] = divmod(long[-right]+flag, 10)
            right += 1
        if flag:
            long[0] = 1
            start = 0  # 开头多1位，如999->1000
        else:
            start = 1
        p = dummy = ListNode(0)
        for i in range(start, len(long)):
            p.next = ListNode(long[i])
            p = p.next
        return dummy.next
# Runtime: 88 ms, faster than 29.86% of Python3 online submissions for Add Two Numbers II.
# Memory Usage: 13.9 MB, less than 6.25% of Python3 online submissions for Add Two Numbers II.


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0
        while l1:
            num1 =  num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        num1 += num2
        p = dummy = ListNode(0)
        for n in str(num1):
            p.next = ListNode(int(n))
            p = p.next
        return dummy.next
# Runtime: 76 ms, faster than 89.98% of Python3 online submissions for Add Two Numbers II.
# Memory Usage: 14 MB, less than 6.25% of Python3 online submissions for Add Two Numbers II.
