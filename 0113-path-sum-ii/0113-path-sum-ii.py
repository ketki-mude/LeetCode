# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        result=[]

        def dfs(root,remaining,path):

            if root is None:
                return False
            
            path.append(root.val)

            if root.left is None and root.right is None:
                if remaining == root.val:
                    result.append(list(path))
     
            dfs(root.left,remaining-root.val,path)
            dfs(root.right,remaining-root.val,path)
           
            path.pop()

        dfs(root,targetSum, [])
        return result




                






















