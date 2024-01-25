class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        ans = []
        for x in nums:
            ans.append((a*x*x) + (b*x) +c)
        ans.sort()
        return ans