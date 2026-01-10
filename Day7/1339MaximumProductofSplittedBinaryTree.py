from TreeNode import TreeNode
from collections import deque
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        mod=10**9+7
        def dfs(root:TreeNode):
            if not root: return 0 
            left_val=dfs(root.left)
            right_val=dfs(root.right)
            root.val=(root.val+left_val+right_val)
            return root.val 
        dfs(root)
        queue=deque([root])
        maximum_sum=float('-inf')
        while queue:
              curr=queue.popleft()
              if curr.left:
                  value=((root.val-curr.left.val)*curr.left.val)
                  maximum_sum=max(maximum_sum,value)
                  queue.append(curr.left)
              if curr.right:
                  value=((root.val-curr.right.val)*curr.right.val)
                  maximum_sum=max(maximum_sum,value)
                  queue.append(curr.right)
        return maximum_sum%mod 
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        mod=10**9+7
        ans=[]
        def dfs(root:TreeNode):
            nonlocal ans
            if not root: return 0 
            left_val=dfs(root.left)
            right_val=dfs(root.right)
            ans.append(root.val+left_val+right_val) 
            return ans[-1] 
        dfs(root)
        total=root.val 
        maximum_sum=float('-inf')
        for s in ans:
            maximum_sum=max(maximum_sum,(total-s)*s)
        return maximum_sum%mod
        
                       
