"""257. Binary Tree Paths
Easy

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

Accepted
341,671
Submissions
655,048"""
def binaryTreePaths(self, root):
    def helper(root, prefix = '', ans = []):
        if root == None:
            return []
        elif ((root.left == None) and (root.right == None)):
            ans.append(prefix + str(root.val))
        ans += helper(root.left, prefix + str(root.val) + "->", ans)
        ans += helper(root.right, prefix + str(root.val) + "->", ans)
        return set(ans)
    return helper(root)