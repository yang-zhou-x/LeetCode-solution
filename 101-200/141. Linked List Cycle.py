'''
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, 
we use an integer pos which represents the position (0-indexed) in the linked list 
where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''

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
