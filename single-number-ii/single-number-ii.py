class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s =  3 * sum(set(nums)) -  sum(nums)
        res = s//2
        return res