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
        fast=head
        slow=head
        is_cycle=False # 判断是否有循环
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow is fast: # fast路程=2*slow路程
                is_cycle=True
                break
        if is_cycle:
            p=head
            while p is not fast:  # 可以画图理解。a | b-a | a 三段
                p=p.next
                fast=fast.next
            return p
        return None
        
# Runtime: 60 ms, faster than 17.64% of Python online submissions for Linked List Cycle II.
