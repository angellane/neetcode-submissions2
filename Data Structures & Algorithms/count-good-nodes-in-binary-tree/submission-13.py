# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        currMax = 0
        if not root:
            return 0

        def dfs(node, currMax):
            nonlocal count
            if not node:
                return 0
            
            if node.val >= currMax:
                count+=1
            currMax = max(currMax, node.val)
            
            dfs(node.left, currMax)
            dfs(node.right, currMax)
            return count
        return dfs(root, currMax)
        



            
        