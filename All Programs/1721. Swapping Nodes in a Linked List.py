# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        store = head
        first = head
        second = head
        i = 1

        while(head.next!= None):
            head = head.next
            i = i + 1
            if(i == k):
                first = head
                second = store
            elif i>k:
                second=second.next

        temp = first.val
        first.val = second.val
        second.val = temp
        return store




        
