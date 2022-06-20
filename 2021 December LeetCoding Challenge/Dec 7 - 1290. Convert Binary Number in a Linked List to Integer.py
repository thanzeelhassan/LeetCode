# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        if head == None:
            return result
        while(head!=None):
            temp = head.val
            result = result * 2
            result = result + pow(temp,2)
            head = head.next
        return result
