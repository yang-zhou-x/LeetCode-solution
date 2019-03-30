# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        p=dummy
        next_=0 # 记录是否进位
        while l1 or l2 or next_:
            if l1:
                next_+=l1.val
                l1=l1.next
            if l2:
                next_+=l2.val
                l2=l2.next
            p.next=ListNode(next_%10)
            p=p.next
            next_//=10
        return dummy.next

# Runtime: 64 ms, faster than 97.72% of Python online submissions for Add Two Numbers.
# Memory Usage: 12 MB, less than 5.16% of Python online submissions for Add Two Numbers.
