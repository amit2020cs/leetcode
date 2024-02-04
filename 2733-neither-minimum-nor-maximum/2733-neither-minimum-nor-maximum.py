class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
        num1 = max(nums)
        num2 = min(nums)
        
        for i in nums:
            if i!= num1 and i !=num2:
                return i
        return -1