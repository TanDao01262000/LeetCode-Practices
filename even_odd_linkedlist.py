# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    Solution 1: 
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return head
        
        odd_head = head
        even_head = even_cur = head.next
        
        while even_cur != None and even_cur.next != None:
            odd_head.next = even_cur.next
            odd_head = odd_head.next
            even_cur.next = odd_head.next
            even_cur = even_cur.next
        
        odd_head.next = even_head
        return head