# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self,root,array):
        if root == None:
            return
        self.postorder(root.left,array)
        self.postorder(root.right,array)
        array.append(root.val)
        return array
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        result = self.postorder(root,array)
        return result        
