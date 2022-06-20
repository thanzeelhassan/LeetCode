# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        temp = head.next
        temp2 = temp.next
        temp3 = head
        head = temp
        head.next = temp3
        temp3.next = temp2

        head.next.next = self.swapPairs(head.next.next)

        return head
