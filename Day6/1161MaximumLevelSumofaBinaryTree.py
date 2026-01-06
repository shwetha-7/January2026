from TreeNode import TreeNode
from collections import deque

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        maxi_val=float('-inf')
        ans=level=0
        queue=deque([root])
        while queue:
              length=len(queue)
              curr_sum=0
              level+=1
              for _ in range(length):
                  curr:TreeNode=queue.popleft()
                  curr_sum+=curr.val 
                  if curr.left:
                      queue.append(curr.left)
                  if curr.right:
                      queue.append(curr.right)
              if maxi_val<curr_sum:
                  maxi_val=curr_sum
                  ans=level 
        return ans 



                      
        