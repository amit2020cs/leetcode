class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 +7
        
        stack = []
        
        dp = [0] * len(arr)
        
        for i in range(len(arr)):
            
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                prevSmaller = stack[-1]
                dp[i] = dp[prevSmaller] + (i - prevSmaller) * arr[i]
            else:
                dp[i] = (i+1) * arr[i]
            
            stack.append(i)
        
        return sum(dp) % MOD