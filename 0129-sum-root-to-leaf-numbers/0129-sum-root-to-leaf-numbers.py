# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        root_to_leaf = 0
        stack = [(root,0)]
        while stack:
            root , curr= stack.pop()
           
            if root is not None:
                curr = curr * 10 + root.val
                
                if root.left is None and root.right is None:
                    root_to_leaf += curr
                else:
                    stack.append((root.right, curr))
                    stack.append((root.left,curr))
        return root_to_leaf