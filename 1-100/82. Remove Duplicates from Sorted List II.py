'''
Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = prev = ListNode('...')
        dummy.next = head
        curr1 = head
        curr2 = head.next
        while curr2:
            if curr1.val != curr2.val:
                prev = prev.next
                curr1 = curr1.next
                curr2 = curr2.next
            else:
                while curr2.next:
                    if curr2.val == curr2.next.val:
                        curr2 = curr2.next
                    else:
                        break
                if curr2.next:  # 最后1个数字不重复时
                    curr1 = curr2.next
                    curr2 = curr1.next
                else:  # 最后1个数字重复时
                    curr1 = curr2 = None
                prev.next = curr1  # 重新建立连接
        return dummy.next
# Runtime: 64 ms, faster than 6.12% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 13.9 MB, less than 5.19% of Python3 online submissions for Remove Duplicates from Sorted List II.

# 简化一下
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = prev = ListNode('...')
        dummy.next = head
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                rm_val = curr.val  # 记录重复的值
                while curr and curr.val == rm_val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return dummy.next
# Runtime: 44 ms, faster than 84.70% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 14 MB, less than 5.19% of Python3 online submissions for Remove Duplicates from Sorted List II.
