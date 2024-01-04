class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lsum = 0
        rsum = 0
        res  = []
        for i in range(n):
            # ans_so_far = sum(nums[i:])
            res.append(abs(sum(nums[i+1:])-sum(nums[:i])))
        return res
            
            
        