class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n, max_sum = len(nums), -1

        for i in range(n):
            for j in range(i+1,n):
                if max([int(k) for k in str(nums[i])]) == max([int(k) for k in str(nums[j])]):
                    max_sum = max(max_sum,nums[i]+nums[j])

        return max_sum
        