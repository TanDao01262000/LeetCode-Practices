# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 1: Using the BFS algorithm on the tree - O(n) runtime complexity, 
    # O(n) space complexity (implement of queue)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        q = [root]
        while q:
            temp = []
            for _ in range(len(q)):
                cur = q.pop(0)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                temp.append(cur.val)
            if temp:
                res.append(temp)
        return res