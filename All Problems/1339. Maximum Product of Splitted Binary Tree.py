# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            ans = dfs(node.left) + dfs(node.right) + node.val
            res.append(ans)
            return ans

        res = []
        sum_all = dfs(root)
        return max(i*(sum_all-i) for i in res) % (10**9 + 7)
