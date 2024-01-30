class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = list(s.split())
        
        res1 = res[-1]
        return len(res1)