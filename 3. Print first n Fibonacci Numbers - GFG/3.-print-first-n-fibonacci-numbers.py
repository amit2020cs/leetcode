#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        res=[]
        
        if n==1:
            res.append(1)
            return res
        elif n==2:
            res.append(1)
            res.append(1)
            return res
        else:
            f1 = 1
            f2 = 1
            res.append(f1)
            res.append(f2)
            count = 2
            while(n>count):
                next = f1+f2
                res.append(next)
                f1 = f2
                f2 = next
                count+=1
        return res
        # your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len (res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends