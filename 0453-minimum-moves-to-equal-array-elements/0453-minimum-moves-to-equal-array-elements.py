class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)
#         if len(set(nums))==1: return 0
#         count = 0
#         while True: 
#             nums.sort()
#             for i in range(len(nums)-1):
#                 nums[i] = nums[i]+1
#             count+=1
#         return count
            


            
            
        