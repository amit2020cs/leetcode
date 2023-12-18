class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        j = 0
        ans = 0
        prev_count = 0
        
        for i in range(n):
            if nums[i] >= left and nums[i] <= right:
                ans += i-j+1
                prev_count = i-j+1
            elif nums[i] < left:
                ans += prev_count
            else:
                j = i+1
                prev_count = 0
        return ans
        