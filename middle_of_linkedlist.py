# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Solution 1: findin' length and move the pointer to the right place - O(n) time complexity and O(1) space complexity
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
            
        curr = head
        for _ in range(length//2):
            curr = curr.next
        return cur