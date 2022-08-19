"""Given the root of a binary tree, invert the tree, and return its root."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        cur = root
        if not cur:
            return
        cur.left, cur.right = cur.right, cur.left
        if cur.left:
            self.invertTree(cur.left)
        if cur.right:
            self.invertTree(cur.right)
        
        return root

        