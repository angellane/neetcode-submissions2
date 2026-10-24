# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.left is None or root.right is None:
            return False

        def dfs(node):
            if not node:
                return False
            if not node.left or not node.right:
                return False

            if node.left and node.left.val < node.val:
                dfs(node.left)
            else:
                return False
            if node.right and node.right.val > node.val:
                dfs(node.right)
            else:
                return False
            return True 
            
            

        return dfs(root)
        