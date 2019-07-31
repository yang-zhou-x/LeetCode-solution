'''
One way to serialize a binary tree is to use pre-order traversal. 
When we encounter a non-null node, we record the node's value. 
If it is a null node, we record using a sentinel value such as #.
     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", 
where # represents a null node.
Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. 
Find an algorithm without reconstructing the tree.
Each comma separated value in the string must be either an integer or a character '#' representing null pointer.
You may assume that the input format is always valid, 
for example it could never contain two consecutive commas such as "1,,3".

Example 1:
Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true

Example 2:
Input: "1,#"
Output: false

Example 3:
Input: "9,#,#,1"
Output: false
'''

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slot = 1  # one empty slot to put the root in it
        nodes = preorder.split(',')
        for node in nodes:
            if slot == 0:  # no empty slot to put the current node
                return False
            if node == '#':  # a null node
                slot -= 1
            else:
                # a non-null node occupies one slot before it creates two more.
                # the net gain is one.
                slot += 1
        return slot == 0
# Runtime: 36 ms, faster than 93.94% of Python3 online submissions for Verify Preorder Serialization of a Binary Tree.
# Memory Usage: 13.8 MB, less than 5.00% of Python3 online submissions for Verify Preorder Serialization of a Binary Tree.
