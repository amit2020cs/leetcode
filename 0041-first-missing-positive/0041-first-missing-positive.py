class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        i = 0
        
        while(i<n):
            if nums[i] ==i+1:
                i+=1
                continue
            if nums[i] <= 0 or nums[i]>n:
                i+=1
                continue
            idx1 = i
            idx2 = nums[i] -1
            
            if(nums[idx1]==nums[idx2]):
                i+=1
                continue
            temp = nums[idx1]
            nums[idx1] = nums[idx2]
            nums[idx2] = temp
        
        
        for j in range(n):
            if nums[j] != j+1:
                return j+1
        
        return n+1
            