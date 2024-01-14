# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nodevalue = []
        
        def dfs(node):
            if node is None:
                return
            nodevalue.append(node.val)
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        nodevalue.sort()
        mindiff = 1e9
        
        for i in range(1, len(nodevalue)):
            mindiff = min(mindiff, nodevalue[i] - nodevalue[i-1])
        
        return mindiff
        