'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        count = 0
        p = head
        while p:
            count += 1
            p = p.next
        if count < 2:
            return head
        k %= count
        if not k:
            return head
        p1, p2 = head, head
        for _ in range(k):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        new_head = p2.next
        p1.next = head
        p2.next = None
        return new_head
# Runtime: 44 ms, faster than 52.42% of Python3 online submissions for Rotate List.
# Memory Usage: 14 MB, less than 5.10% of Python3 online submissions for Rotate List.
