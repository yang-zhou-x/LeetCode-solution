'''
Sort a linked list using insertion sort.
A graphical example of insertion sort. 
The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list

Algorithm of Insertion Sort:
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, 
finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = dummy = ListNode(0)
        curr = dummy.next = head
        while curr and curr.next:
            val = curr.next.val
            if curr.val < val:
                curr = curr.next
                continue
            else:
                if p.next.val > val:
                    p = dummy
                while p.next.val < val:
                    p = p.next
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = p.next
                p.next = tmp
        return dummy.next
# Runtime: 128 ms, faster than 94.83% of Python3 online submissions for Insertion Sort List.
# Memory Usage: 15.8 MB, less than 8.04% of Python3 online submissions for Insertion Sort List.
