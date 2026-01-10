from TreeNode import TreeNode

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        maxDepth={None:-1}
        def dfs(curr_node:TreeNode,parent:TreeNode=None):
            nonlocal maxDepth
            if curr_node:
               maxDepth[curr_node]=maxDepth[parent]+1
               dfs(curr_node.left,curr_node)
               dfs(curr_node.right,curr_node)
        dfs(root)
        max_depth=max(maxDepth.values())
        def answer(curr_node:TreeNode):
            if not curr_node or maxDepth.get(curr_node,None)==max_depth:
                return curr_node 
            left,right=answer(curr_node.left),answer(curr_node.right)
            return curr_node if left and right else left or right 
        return answer(root)
                
            
            