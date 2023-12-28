# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        dia = 0
        
        def longest_dai(node):
            if not node:
                return 0
            nonlocal dia
            
            left_path = longest_dai(node.left)
            right_path = longest_dai(node.right)
            
            dia = max(dia, left_path+ right_path)
            
            return max(left_path, right_path) +1
        
        longest_dai(root)
        
        return dia
        