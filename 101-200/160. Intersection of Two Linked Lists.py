'''
Write a program to find the node at which the intersection of two singly linked lists begins.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. 
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. 
From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, 
while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
'''

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
        size1, size2 = 0, 0
        p1, p2 = headA, headB
        while p1:
            size1 += 1
            p1 = p1.next
        while p2:
            size2 += 1
            p2 = p2.next
        if size1 > size2:
            for _ in range(size1-size2):
                headA = headA.next
        if size2 > size1:
            for _ in range(size2-size1):
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
# Runtime: 188 ms, faster than 99.85% of Python online submissions for Intersection of Two Linked Lists.
# Memory Usage: 41 MB, less than 29.10% of Python online submissions for Intersection of Two Linked Lists.
