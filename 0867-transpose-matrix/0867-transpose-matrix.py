class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # m = len(matrix)
        # n = len(matrix[0])
        # res = [[0]*m for _ in range(n)]
        # for i in range(m):
        #     for j in range(n):
        #         res[i][j]=matrix[j][i]
        # return res
    
        n=len(matrix)
        m=len(matrix[0])
        ans=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j]=matrix[j][i]
        return ans  