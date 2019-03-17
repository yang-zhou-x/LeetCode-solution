# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        
        level=[root]
        ans=[]
        fromRight=False
        while level:
            vals=[node.val for node in level]
            if fromRight:
                vals.reverse()
            ans.append(vals)
            fromRight=not fromRight
            lrPairs=[(node.left,node.right) for node in level]
            level=[node for lr in lrPairs for node in lr if node]
        return ans
        
# Runtime: 36 ms, faster than 99.52% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
