class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumOfRight=sum(nums)
        sumOfLeft=0
        for i in range(len(nums)):
            if i>0:
                sumOfLeft+=nums[i-1]
            sumOfRight-=nums[i]
            if sumOfLeft==sumOfRight:
                return i
        return -1
        