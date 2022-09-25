class Solution:
    def sortSentence(self, s: str) -> str:
        a=[]
        for i in s:
            if i.isdigit()==True:
                a.append(i)   

            
        res = ''.join([i for i in s if not i.isdigit()])
        li = list(res.split(" "))
        test = [int(i) for i in a] 
        
        ans = [0]*len(test)
        for i in range(len(test)):                
                j=test[i]
                ans[j-1]=li[i]

    
        Str = ' '.join([str(elem) for elem in ans])
        return Str
 
        