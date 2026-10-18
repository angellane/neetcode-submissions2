# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
            
        qq = deque([q])
        pq = deque([p])

        while pq and qq:
            for i in range(len(qq)):
                node = qq.popleft()
                node2 = pq.popleft()
                if node.val != node2.val:
                    return False

                if (node.left is None) != (node2.left is None):
                    return False
                if (node.right is None) != (node2.right is None):
                    return False
                if node.left: 
                    qq.append(node.left)
                if node2.left :
                    pq.append(node2.left)
                if node.right :
                    qq.append(node.right)
                if node2.right :
                    pq.append(node2.right)
            
        return True if not qq and not pq else False