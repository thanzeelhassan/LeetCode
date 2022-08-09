"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def helper(self, root, arr):
        if root == None:
            return arr
        arr.append(root.val)
        if root.children != None:
            for i in root.children:
                arr = self.helper(i,arr)
        return arr
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        arr = self.helper(root,arr)
        return arr