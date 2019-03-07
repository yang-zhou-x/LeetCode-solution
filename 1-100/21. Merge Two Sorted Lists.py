# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans=ListNode(0)
        p=ans
        while l1 and l2:
            if l1.val<l2.val:
                p.next=ListNode(l1.val)
                l1=l1.next
            else:
                p.next=ListNode(l2.val)
                l2=l2.next
            p=p.next
        if l1:
            p.next=l1
        if l2:
            p.next=l2
        return ans.next
       
       
# Runtime: 24 ms, faster than 100.00% of Python online submissions for Merge Two Sorted Lists.
# Memory Usage: 11.1 MB, less than 5.04% of Python online submissions for Merge Two Sorted Lists.
 
