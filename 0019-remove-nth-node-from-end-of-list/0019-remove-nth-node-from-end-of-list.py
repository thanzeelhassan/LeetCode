# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = head
        
        if head == None:
            return head
        for i in range(n):
            head = head.next
            
        start = result
        
        if head == None:
            return start.next
        while(head.next != None):
            head = head.next
            start = start.next
        
        start.next = start.next.next
        
        return result
        