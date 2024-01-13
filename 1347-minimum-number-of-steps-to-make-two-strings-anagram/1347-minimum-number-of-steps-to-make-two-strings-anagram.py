class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        count = 0 
        
        for i in t:
            if i in s:
                s = s.replace(i,"",1)
            else:
                count+=1
        return count