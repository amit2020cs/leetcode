class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        a = True
        while a:
            if original in nums:
                original = original * 2
            else:
                a = False
        return original
        