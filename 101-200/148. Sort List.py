# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        p=head
        nums=[]
        while p:
            nums.append(p.val)
            p=p.next
        nums.sort()
        p=head
        for n in nums:
            p.val=n
            p=p.next
        return head
        
# Runtime: 88 ms, faster than 99.08% of Python3 online submissions for Sort List.
# Memory Usage: 20.3 MB, less than 16.07% of Python3 online submissions for Sort List.
