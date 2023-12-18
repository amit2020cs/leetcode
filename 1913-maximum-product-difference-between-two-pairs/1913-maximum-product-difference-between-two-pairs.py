class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        r = nums[-1]*nums[-2]
        l = nums[0]*nums[1]
        return r-l