# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        b = []
        while(head!=None):
            arr.append(head.val)
            b.append(head.val)
            head = head.next
        arr.reverse()
        if arr == b:
            return True
        return False