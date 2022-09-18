class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum(1 for n in nums if n<i) for i in nums]
