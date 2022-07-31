# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Solution 1: using recursion to solve, O(n) time and space
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return root
        res = [root.val]
        if root.left:
            res += self.preorderTraversal(root.left)
        if root.right:
            res += self.preorderTraversal(root.right)
        
        return res

# or
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        res = []
        res.append(root.val)
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res
    

    # Solution 2: iterative using stack, O(n) for both
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        
        res =[]
        if root:
            stack = [root]

            while stack:
                cur = stack.pop()
                
                if cur:
                    res.append(cur.val)
                    stack += [cur.right, cur.left]
        return res
