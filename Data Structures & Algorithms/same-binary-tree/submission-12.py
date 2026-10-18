# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        pq = deque([p])
        qq = deque([q])

        while pq and qq:
            for i in range(len(qq)):
                node = pq.popleft()
                node2 = qq.popleft()
                if not node or not node2:
                    return True 
                if node.val != node2.val:
                    return False
                if node.left and node2.left and node.left.val == node2.left.val:
                    pq.append(node.left)
                    qq.append(node2.left)
                if node.right and node2.right and node.right.val == node2.right.val:
                    pq.append(node.right)
                    qq.append(node2.right)
        
        return True if not pq and not qq else False












  #      def dfs(p, q):
  #          if not p:
  #              return False
  #          if not q:
  #              return False
  #          if p.left == q.left and p.right == q.right:
  #              return True 

 #           dfs(p.left, q.left)
  #          dfs(p.right, q.right)
            
        
   #     dfs(p,q)
        



        