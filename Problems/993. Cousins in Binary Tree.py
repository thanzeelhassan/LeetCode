# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node, parent, depth, value):
            if node:
                if node.val == value:
                    return depth, parent
                return dfs(node.left, node, depth + 1, value) or dfs(node.right, node, depth + 1, value)

        dx, px = dfs(root, None, 0, x)
        dy, py = dfs(root, None, 0, y)
        return dx == dy and px != py
