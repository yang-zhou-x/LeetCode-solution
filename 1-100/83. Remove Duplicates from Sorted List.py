'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
'''

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                rm_val = curr.val
                p = curr.next.next
                while p and p.val == rm_val:
                    p = p.next
                curr.next = p
                curr = curr.next
            else:
                curr = curr.next
        return head
# Runtime: 52 ms, faster than 19.57% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 14 MB, less than 5.13% of Python3 online submissions for Remove Duplicates from Sorted List.

# 简化一下
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
# Runtime: 48 ms, faster than 62.54% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 14 MB, less than 5.13% of Python3 online submissions for Remove Duplicates from Sorted List.
