#User function Template for python3

class Solution:
    def findNth(self,N, M:int=9):
        alpha, beta = 0,1
        while(N >0):
            alpha+=(beta * (int(N)%M))
            N/=M
            beta*=10
        return alpha
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for i in range(0,t):
    n=int(input())
    obj=Solution()
    s=obj.findNth(n)
    print(s)
# } Driver Code Ends