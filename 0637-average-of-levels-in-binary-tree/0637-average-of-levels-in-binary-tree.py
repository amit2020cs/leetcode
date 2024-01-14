# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque()
        q.append(root)
        while q:
            level = len(q)
            sumAtCurrentLevel = 0
            
            for _ in range(len(q)):
                node = q.popleft()
                sumAtCurrentLevel += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(sumAtCurrentLevel/level)
        return ans
                