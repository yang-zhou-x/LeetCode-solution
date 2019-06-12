'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        nums = []
        p = head
        while p:
            nums.append(p.val)
            p = p.next
        nums.sort()
        p = head
        for n in nums:
            p.val = n
            p = p.next
        return head
# Runtime: 80 ms, faster than 99.91% of Python3 online submissions for Sort List.
# Memory Usage: 20.5 MB, less than 91.55% of Python3 online submissions for Sort List.
