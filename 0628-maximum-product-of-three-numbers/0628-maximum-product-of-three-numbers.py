class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        num = nums[-3:]
        curr1 = nums[0]*nums[1]*nums[len(nums) -1]
        curr = 1
        for i in num:
            curr*=i
        return max(curr1, curr)
        