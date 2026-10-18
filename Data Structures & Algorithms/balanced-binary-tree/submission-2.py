# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        leftLevel = 0 
        rightLevel = 0
        q = deque([root])
        if not root:
            return True

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    leftLevel +=1
                    
                if node.right:
                    q.append(node.right)
                    rightLevel += 1
            if leftLevel + 1 > rightLevel or rightLevel + 1 > leftLevel:
                return False
        return True
                


             



        