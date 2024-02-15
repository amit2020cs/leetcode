class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        
        pre_sum = 0
        
        ans = -1
        
        for num in nums:
            
            if num < pre_sum:
                ans = num + pre_sum 
            pre_sum += num
            
        return ans
        