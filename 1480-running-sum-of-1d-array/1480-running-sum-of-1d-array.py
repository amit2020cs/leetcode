class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        sums = nums[0]
        for i in range(1,len(nums)):
            sums = sums + nums[i]
            result.append(sums)
        return result