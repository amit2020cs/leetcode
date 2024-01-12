class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        s1 = s[:n//2]
        s2 = s[n//2:]
        count1 = 0
        count2 = 0 
        
        for i in s1:
            if i in "aeiouAEIOU":
                count1+=1
        for i in s2:
            if i in "aeiouAEIOU":
                count2+=1
                
        return count1==count2
                
        