class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res1 = any(target in sublist for sublist in matrix)
        return res1