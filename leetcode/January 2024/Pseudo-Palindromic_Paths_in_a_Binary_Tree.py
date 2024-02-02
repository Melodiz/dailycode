# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root):
        return self.rec(root, 0)

    def rec(self, node, path):
        if not node:
            return 0

        path ^= 1 << node.val

        if not node.left and not node.right:
            return 1 if path & (path - 1) == 0 else 0

        return self.rec(node.left, path) + self.rec(node.right, path)

