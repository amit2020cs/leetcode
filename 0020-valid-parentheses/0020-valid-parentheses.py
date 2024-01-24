class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(','{','[']
        right = [')',"}",']']
        
        stack = []
        
        for l in s:
            if l in left:
                stack.append(l)
            elif l in right:
                if len(stack)<=0:
                    return False
                if left.index(stack.pop()) != right.index(l):
                    return False
        return len(stack) == 0
                    
                    