# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        temp = max(nums)
        i = nums.index(temp)
        root = TreeNode(temp)
        l = nums[:i]
        r = nums[i+1:]
        root.left = self.constructMaximumBinaryTree(l)
        root.right = self.constructMaximumBinaryTree(r)    
        return root