'''
Implement an iterator over a binary search tree (BST). 
Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.
 
Example:
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 
Note:
next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, 
there will be at least a next smallest number in the BST when next() is called.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# 一次性将BST转换为数组
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nums = []
        self.in_order(root)
        self.idx = 0
        
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            self.nums.append(node.val)
            self.in_order(node.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.idx < len(self.nums):
            self.idx += 1
            return self.nums[self.idx - 1]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.idx < len(self.nums)
# Runtime: 88 ms, faster than 79.94% of Python3 online submissions for Binary Search Tree Iterator.
# Memory Usage: 20.3 MB, less than 5.39% of Python3 online submissions for Binary Search Tree Iterator.

# 一边执行，一边遍历BST
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.dfs(root)
    
    def dfs(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()  # 当前最小的
        self.dfs(node.right)
        return node.val
        
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack != []
# Runtime: 92 ms, faster than 61.03% of Python3 online submissions for Binary Search Tree Iterator.
# Memory Usage: 20.9 MB, less than 5.39% of Python3 online submissions for Binary Search Tree Iterator.
