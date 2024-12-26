# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,array):
        if root == None:
            return
        array.append(root.val)
        self.preorder(root.left,array)
        self.preorder(root.right,array)
        return array
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        result = self.preorder(root,array)
        return result
