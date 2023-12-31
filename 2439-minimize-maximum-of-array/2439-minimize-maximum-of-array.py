class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix  = 0
        ans = 0
        for i in range(len(nums)):
            prefix = prefix + nums[i]
            avg = prefix/(i+1)
            if avg > ans:
                ans = avg
        return ceil(ans)
        