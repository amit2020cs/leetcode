class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(len(arr) - 1, -1, -1):
            m = 0
            for j in range(i, min(i + k, len(arr))):
                dp[i] = max(dp[i], (m := max(m, arr[j])) * (j - i + 1) + dp[j + 1])
        return dp[0]