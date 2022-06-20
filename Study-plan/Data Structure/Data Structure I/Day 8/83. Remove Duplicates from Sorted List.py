# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head
        if head == None:
            return head
        prev = head
        head = head.next
        while(head!= None):
            if head.val == prev.val:
                head = head.next
            else:
                prev.next = head
                prev = head
                head = head.next
        prev.next = None
        return result
