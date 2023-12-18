# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None or root.val == key:
            return root
 
        # Key is greater than root's key
        if root.val < key:
            return self.searchBST(root.right,key)

        # Key is smaller than root's key
        return self.searchBST(root.left,key)
        