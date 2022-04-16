# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            if root:
                # Then recur on left child
                traverse(root.left)
                
                # Finally recur on right child
                traverse(root.right)
                # First print the data of node
                a.append(root.val)
        a = []
        traverse(root)
        return a
        