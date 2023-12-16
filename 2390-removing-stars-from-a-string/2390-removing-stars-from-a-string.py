class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        res = []
        
        for i in s:
            if i !='*':
                res.append(i)
            else:
                res.pop()
        # for ele in res:
            # str1 += ele
        str1 = ""
        # str1.join(res)
        return str1.join(res)
                
        