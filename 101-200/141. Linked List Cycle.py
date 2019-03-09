# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while slow != fast:  # while slow is not fast:
                slow = slow.next  # 类似追及问题
                fast = fast.next.next
            return True
        except:
            return False
            
# Runtime: 40 ms, faster than 99.24% of Python online submissions for Linked List Cycle.
# Memory Usage: 17.1 MB, less than 40.43% of Python online submissions for Linked List Cycle.
