# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #check if root is empty

        if root is None:
            return False

        # check it is leaf
        if root.right is None and root.left is None:
            return targetSum == root.val

        remaining = targetSum - root.val

        return (
            self.hasPathSum(root.left,remaining)
            or
            self.hasPathSum(root.right,remaining)        

        )


        