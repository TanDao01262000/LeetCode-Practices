# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 1: Using the BFS algorithm on the tree - O(n) runtime complexity, 
    # O(n) space complexity (implement of queue)
    def level_order_traversal(self, root: TreeNode) -> list[list[int]]:
        res = []
        q = Collection.deque()
        q.append(root)
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popLeft()
                if node:
                    level.append(node.val)
                    q.append(node.left)         
                    q.append(node.right)   
            if level:
                res.append(level)
        return res      