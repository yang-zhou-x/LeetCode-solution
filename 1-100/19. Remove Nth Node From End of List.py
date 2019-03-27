# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p=head
        count=0
        while p:
            count+=1
            p=p.next
        if count<2:
            return None
        if count==n:
            return head.next
        p=head
        for i in range(count-n-1): # 到达被删节点的前一个节点
            p=p.next
        p.next=p.next.next
        return head
        
# Runtime: 40 ms, faster than 90.04% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13 MB, less than 5.60% of Python3 online submissions for Remove Nth Node From End of List.
