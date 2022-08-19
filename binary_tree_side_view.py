"""Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #  Solution 1: implementing binary tree level traversal
    #  and extract the rightmost element on each level (which we can see from the right side)
    #  - O(n) for both runtime and space complexity
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        if not root:
            return res
        
        q = [root]
        while q:
            temp = 0
            for _ in range(len(q)):  #  level traversal in BT with BFT
                cur = q.pop(0)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            temp = cur.val  # keep track of the rightmost element of each level
            res.append(temp)
        return res  
