class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        s = set()
        while nums:
            min1 =min(nums)
            max1 = max(nums)
            avg = (min1+max1)/2
            s.add(avg)
            nums.remove(min1)
            nums.remove(max1)
        return len(s)