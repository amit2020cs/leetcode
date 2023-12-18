class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        i = 0
        j = 0
        num_0 = 0
        while j < n:
            if nums[j] == 0:
                num_0 +=1
            
            while num_0 ==2:
                if nums[i] == 0:
                    num_0-=1
                i+=1
            res = max(res,j-i+1)
            j+=1
        return res
        