class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        def function(x, a, b,c ):
            
            res = a*(x*x) + b*x +c
            return res
        ans = []
        for i in nums:
            ans.append(function(i,a,b,c))
        ans.sort()
        return ans