# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def Helper(node,max_val):
            if node == None:
                return 0
            if node.val >= max_val:
                return 1 + Helper(node.right,node.val) + Helper(node.left,node.val)
            else :
                return Helper(node.right,max_val) + Helper(node.left,max_val)
        return 1 + Helper(root.right,root.val) + Helper(root.left,root.val)
        
