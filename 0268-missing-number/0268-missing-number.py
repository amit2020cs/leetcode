class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalsum = (n)*(n+1)/2
        sumoflist = sum(nums)
        return int(totalsum-sumoflist)
        