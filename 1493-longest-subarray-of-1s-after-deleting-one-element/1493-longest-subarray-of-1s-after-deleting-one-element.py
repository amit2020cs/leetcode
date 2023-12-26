class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = 0
        longwid = 0
        start = 0
        for i in range(len(nums)):
            zero+=(nums[i]==0)
            
            while zero > 1:
                zero -= nums[start]==0
                start+=1
            longwid = max(longwid,i - start)
        
        return longwid
            
                
        
        