class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s.split())[::-1]
        res = " "
        return res.join(l)
        
        