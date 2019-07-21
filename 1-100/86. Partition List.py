'''
Given a linked list and a value x, 
partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p1 = lt = ListNode(0)
        p2 = gt = ListNode(0)
        while head:
            if head.val < x:
                p1.next = ListNode(head.val)
                p1 = p1.next
            else:
                p2.next = ListNode(head.val)
                p2 = p2.next
            head = head.next
        p1.next = gt.next
        return lt.next
# Runtime: 40 ms, faster than 66.97% of Python3 online submissions for Partition List.
# Memory Usage: 14 MB, less than 5.88% of Python3 online submissions for Partition List.
