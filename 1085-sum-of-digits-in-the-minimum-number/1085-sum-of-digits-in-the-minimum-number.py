class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        num = min(nums)
        
        res = 0
        
        for i in str(num):
            res+=(int(i))
        
        if res%2==0:
            return 1
        return 0
        