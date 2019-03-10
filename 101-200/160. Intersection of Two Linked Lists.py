# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        size1,size2=0,0
        p1,p2=headA,headB
        while p1:
            size1+=1
            p1=p1.next
        while p2:
            size2+=1
            p2=p2.next
        if size1>size2:
            for _ in range(size1-size2):
                headA=headA.next
        if size2>size1:
            for _ in range(size2-size1):
                headB=headB.next
        while headA!=headB:
            headA=headA.next
            headB=headB.next
        
        return headA

# Runtime: 188 ms, faster than 99.85% of Python online submissions for Intersection of Two Linked Lists.
# Memory Usage: 41 MB, less than 29.10% of Python online submissions for Intersection of Two Linked Lists.
