# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def height(root):
            if root == None:
                return -1
            left = height(root.left)
            right = height(root.right)
            self.ans = max(self.ans, 2+left + right)
            return 1 + max(left,right)
        height(root)
        return self.ans
        
