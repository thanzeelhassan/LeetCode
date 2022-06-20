# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head

        while(head!= None and head.val == val):
            head = head.next

        result = head

        while(head!=None):
            if head.next != None:
                if head.next.val == val:
                    if head.next.next == None:
                        head.next = None
                    else:
                        head.next = head.next.next
                else:
                    head = head.next
            else:
                head = head.next
        return result
            
