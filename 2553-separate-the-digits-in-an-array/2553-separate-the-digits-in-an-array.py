class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s = ""
        for i in nums:
            s+=str(i)
        res = []
        for i in s:
            res.append(int(i))
            
        return res
        