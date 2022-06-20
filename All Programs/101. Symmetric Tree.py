# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root1,root2):
        if root1 == None:
            if root2 == None:
                return True
            else:
                return False
        elif root2 == None:
            return False
        elif root1.val == root2.val:
            return self.helper(root1.left,root2.right) and self.helper(root1.right,root2.left)
        else:
            return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.helper(root.left,root.right)
