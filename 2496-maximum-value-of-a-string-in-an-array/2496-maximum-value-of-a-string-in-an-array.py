class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0
        for i in strs:
            if i.isdigit():
                res = max(res, int(i))
            else:
                n = len(i)
                res = max(res,n)
        return res
                
        