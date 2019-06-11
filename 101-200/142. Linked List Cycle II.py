'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the 
position (0-indexed) in the linked list where tail connects to. If pos is -1, 
then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it without using extra space?
'''

# 解法1：两指针，类似追及
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        is_cycle = False  # 判断是否有循环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:  # fast路程=2*slow路程
                is_cycle = True
                break
        if is_cycle:
            p = head
            while p is not fast:  # 可以画图理解。a | b-a | a 三段
                p = p.next  # 其中位置a处为循环点
                fast = fast.next
            return p
        return None
# Runtime: 36 ms, faster than 95.96% of Python online submissions for Linked List Cycle II.
# Memory Usage: 18.2 MB, less than 73.15% of Python online submissions for Linked List Cycle II.

# 解法2：用set存储节点
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cahce = set()
        p = head
        while True:
            if p is None:
                return None
            elif p not in cahce:
                cahce.add(p)
                p = p.next
            else:
                break
        return p
# Runtime: 36 ms, faster than 95.96% of Python online submissions for Linked List Cycle II.
# Memory Usage: 18.7 MB, less than 14.99% of Python online submissions for Linked List Cycle II.
