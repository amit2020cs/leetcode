class Solution:
    def calculate(self, s: str) -> int:
        inner , outer, res, opt = 0,0,0,'+'
        
        for c in s + '+':
            if c==' ': continue
            if c.isdigit():
                inner = 10* inner +int(c)
                continue
            if opt == '+':
                res +=outer
                outer = inner
            elif opt =='-':
                res+=outer
                outer = -inner
            elif opt =='*':
                outer = outer * inner
            elif opt =='/':
                outer = int(outer / inner)
            inner,  opt = 0,c
        return res + outer
            