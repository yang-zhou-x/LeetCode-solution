'''
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        k = n - m + 1
        p1 = dummy = ListNode(0)
        dummy.next = head
        while m > 1:
            p1 = p1.next  # 反转部分的前一个节点
            m -= 1
        prev = None  # 开始反转
        p2 = curr = p1.next
        while k > 0:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            k -= 1
        p2.next = curr  # 拼接
        p1.next = prev  # 拼接
        return dummy.next
# Runtime: 36 ms, faster than 68.90% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 13.9 MB, less than 5.04% of Python3 online submissions for Reverse Linked List II.
