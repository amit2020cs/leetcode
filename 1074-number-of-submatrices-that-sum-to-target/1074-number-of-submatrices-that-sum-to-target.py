class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        answer = 0
        for r1 in range(len(matrix)):
            sums = [0] * len(matrix[0])
            for r2 in range(r1, len(matrix)):
                sumFreq, rowSum = {0: 1}, 0
                for c in range(len(matrix[0])):
                    rowSum += matrix[r2][c]
                    sums[c] += rowSum
                    answer += sumFreq.get(sums[c] - target, 0)
                    sumFreq[sums[c]] = sumFreq.get(sums[c], 0) + 1
        return answer