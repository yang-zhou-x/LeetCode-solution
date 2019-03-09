# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:#没有或只有1个节点时
            return True
        
        # 2个及以上节点时：
        slow=head
        fast=head
        prev=None # 用于翻转链表
        while fast and fast.next:#fast为最后1个节点或None时停止循环
            fast=fast.next.next
            tmp=slow.next
            slow.next=prev
            prev=slow # 翻转链表
            slow=tmp
        
        if fast:#奇数个节点时，fast为最后1个节点；偶数个节点时，fast为None
            slow=slow.next
        
        while slow:
            if slow.val!=prev.val:
                return False
            slow=slow.next # slow是链表的后半段
            prev=prev.next # prev是链表前半段的翻转
        
        return True
        
# Runtime: 72 ms, faster than 94.06% of Python online submissions for Palindrome Linked List.
# Memory Usage: 30 MB, less than 66.49% of Python online submissions for Palindrome Linked List.
