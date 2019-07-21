'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted linked list: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
'''

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        def helper(left, right):
            if left > right:
                return None
            mid = (left + right) >> 1
            node = TreeNode(nums[mid])
            if left == right:  # 最后1个
                return node
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            return node
        return helper(0, len(nums) - 1)
# Runtime: 128 ms, faster than 82.60% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
# Memory Usage: 20.4 MB, less than 5.07% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
