class Solution:
    def removeVowels(self, s: str) -> str:
        v = ['a','e','i','o','u']
        S = list(s)
        for i in s:
            if i in v:
                S.remove(i)
        s1 = ""
        
        for  i in S:
            s1+=i
            
        return s1
            
        