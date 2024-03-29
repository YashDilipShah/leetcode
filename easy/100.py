"""
100. Same Tree
Easy

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false

 

Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inOrder(root):
            traversal = []
            if root.left != None:
                traversal = inOrder(root.left) + traversal
            traversal = [None] + traversal
            traversal.append(root.val)
            if root.right != None:
                traversal = traversal + inOrder(root.right)
            traversal = traversal + [None]
            return traversal
        if p and q:
            return inOrder(p) == inOrder(q)
        elif p == None and q == None:
            return True
        else:
            return False