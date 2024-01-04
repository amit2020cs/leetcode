class Solution:
    
    def helper(self,nums):
        
        last, now = 0, 0
        
        for i in nums:
            last, now = now, max(last + i, now)
                
        return now
    
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]), self.helper(nums[:-1]))
        
        

   
        