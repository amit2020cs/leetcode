class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_map = {"(": ")","[": "]","{": "}"}
        
        open_brac = set(["(","[","{"])
        
        stack = []
        
        for i in s:
            if i in open_brac:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                    stack.pop()
            else:
                return False
        return stack == []
                
                    
                    