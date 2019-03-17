# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans=[]
        if root:
            level=[root]
            while level:
                ans.append([node.val for node in level])
                lrPair=[(node.left,node.right) for node in level]
                level=[node for lr in lrPair for node in lr if node]
        return ans

# Runtime: 40 ms, faster than 96.15% of Python3 online submissions for Binary Tree Level Order Traversal.
