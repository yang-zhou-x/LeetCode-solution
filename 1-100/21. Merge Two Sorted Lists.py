'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# python版本
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)  # dummy head
        p = ans
        while l1 and l2:
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return ans.next
# Runtime: 24 ms, faster than 100.00% of Python online submissions for Merge Two Sorted Lists.
# Memory Usage: 11.1 MB, less than 5.04% of Python online submissions for Merge Two Sorted Lists.
 
# python3版本
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
            p = p.next
        p.next = l1 or l2
        return dummy.next
# Runtime: 44 ms, faster than 82.39% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13 MB, less than 95.66% of Python3 online submissions for Merge Two Sorted Lists.
