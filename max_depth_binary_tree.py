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
    

    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        #Solution 2: Using the BFS with the implementation of queue - O(n) time and space complexity
        max_depth = 0

        if not root:
            return max_depth
        
        q = [root]
        
        while q:
            for _ in range(len(q)):
                cur = q.pop()
                if cur:
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            max_depth += 1
 

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        # Solution 3: using DFS with stack of a list: one for node and one for depth level of it - O(n) for both runtime and space complexity
        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
            return max_depth