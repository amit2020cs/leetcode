class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        odd = even = 0
        for a in nums:
            odd ,even = [max(odd, even - a), max(even, odd+a)]
        
        return even
        
        # odd = even = 0
        # for a in A:
        #     odd, even = [max(odd, even - a), max(even, odd + a)]
        # return even