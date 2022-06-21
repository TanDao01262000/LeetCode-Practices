# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 1: Recursively check each branch, and using max for choosing the longest branch - O(n) time and O(1) space
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if not root:
            return max_depth
        if root.left is None and root.right is None:
            return 1
        max_depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return max_depth