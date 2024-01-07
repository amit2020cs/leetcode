class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        m , n= nums[0],nums[-1]
        ans = n - m
        for i in range(len(nums)-1):
            a , b = nums[i], nums[i+1]
            ans = min(ans,max(n-k, a+k) - min(m+k,b-k))
        return ans