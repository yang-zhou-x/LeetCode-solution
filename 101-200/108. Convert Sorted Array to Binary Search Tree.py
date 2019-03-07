# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def aux(left,right):
            if left<=right:
                mid=(left+right)//2
                root=TreeNode(nums[mid])
                root.left=aux(left,mid-1)
                root.right=aux(mid+1,right)
            else:
                return None
            return root
        return aux(0,len(nums)-1)
        
# Runtime: 44 ms, faster than 99.63% of Python online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 14.8 MB, less than 61.85% of Python online submissions for Convert Sorted Array to Binary Search Tree.
 
