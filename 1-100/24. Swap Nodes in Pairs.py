'''
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
'''

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(0)
        dummy.next = head  # prev->swap1->swap2->swap2.next
        while prev.next and prev.next.next:
            swap1 = prev.next
            swap2 = swap1.next
            prev.next, swap2.next, swap1.next = swap2, swap1, swap2.next
            prev = swap1
        return dummy.next
# Runtime: 40 ms, faster than 18.74% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 14 MB, less than 5.21% of Python3 online submissions for Swap Nodes in Pairs.
