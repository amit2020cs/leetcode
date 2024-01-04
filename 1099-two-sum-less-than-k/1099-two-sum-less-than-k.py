class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = -1
        for i in range(len(nums)):
            j = bisect_left(nums, k - nums[i], i+1) -1
            if j > i:
                ans = max(ans, nums[i]+nums[j])
                
        return ans
                
                
                
                
                
#         while i<j:
            
#             mid = (i+j)//2
            
#             if nums[i]+nums[mid]> k:
#                 j-=1
#             if nums[i]+nums[mid]<k:
#                 i+=1
#             else:
#                 return nums[i]+nums[j]
#         return -1
                
        