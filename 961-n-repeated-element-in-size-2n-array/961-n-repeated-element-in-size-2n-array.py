class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                return i
        