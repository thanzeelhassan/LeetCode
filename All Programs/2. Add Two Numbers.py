# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(l1):
            temp = l1
            list1 = []
            while l1:
                list1.append(l1.val)
                l1 = l1.next
            list1.reverse()
            s1 =""
            for item in list1:
                s1 += str(item)
            s1= int(s1)
            return s1

        a = helper(l1)
        b = helper(l2)
        c = a + b
        c = str(c)
        reversed(c)
        head = None
        for i in c:
            new_node = ListNode(int(i))
            new_node.next = head
            head = new_node
        return head
        
