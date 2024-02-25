class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        num1 = max(nums)
        idx = nums.index(num1)
        nums.remove(num1)
        num2 = max(nums)
        
        if num2*2<= num1:
            return idx
        return -1