# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddHead=ListNode(0) #奇数链表
        evenHead=ListNode(0) #偶数链表
        odd=oddHead #指针
        even=evenHead #指针
        isOdd=True #确认奇偶位
        while head:
            if isOdd:
                odd.next=head
                odd=odd.next
            else:
                even.next=head
                even=even.next
            head=head.next
            isOdd=not isOdd
        even.next=None #偶数链表最后为None
        odd.next=evenHead.next # 拼接
        
        return oddHead.next
        
# Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Odd Even Linked List.
