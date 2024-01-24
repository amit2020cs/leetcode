class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        
        max_index1 = max(min_index,max_index)
        min_index1 = min(min_index,max_index)
        
        left_idx = len(nums) - min_index1
        r_idx = len(nums)+1 + min_index1 - max_index1
        
        return min(max_index1+1, left_idx,r_idx)
        
        
        
            
        