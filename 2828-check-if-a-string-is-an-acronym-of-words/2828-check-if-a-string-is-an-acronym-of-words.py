class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        S = ""
        
        for i in words:
            S+=i[0]
        if S==s:
            return True
        return False