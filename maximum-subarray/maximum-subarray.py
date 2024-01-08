class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsofar = nums[0]
        maxend = 0
        for i in range(0,len(nums)):
            maxend = maxend+nums[i]
            if maxsofar < maxend:
                maxsofar = maxend
            if maxend <0:
                maxend = 0
        return maxsofar
    
        