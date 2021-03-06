'''
Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# 解法1，O(N*log(k))，两两合并
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge2lists(list1, list2):
            dummy = ListNode(0)
            p = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    p.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    p.next = ListNode(list2.val)
                    list2 = list2.next
                p = p.next
            if list1:
                p.next = list1
            if list2:
                p.next = list2
            return dummy.next

        amount = len(lists)
        interval = 1
        while amount > interval:
            for i in range(0, amount-interval, interval*2):
                lists[i] = merge2lists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if amount > 0 else lists
# Runtime: 184 ms, faster than 21.71% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 26.8 MB, less than 5.03% of Python3 online submissions for Merge k Sorted Lists.

# 解法2，O(N*log(N))，取出全部数字直接排序，再生成链表
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nums = []
        for l in lists:
            while l:
                nums.append(l.val)
                l = l.next
        dummy = ListNode(0)
        p = dummy
        for n in sorted(nums):
            p.next = ListNode(n)
            p = p.next
        return dummy.next
# Runtime: 72 ms, faster than 89.23% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 17.4 MB, less than 15.49% of Python3 online submissions for Merge k Sorted Lists.
