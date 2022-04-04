#User function Template for python3

class Solution:
    def findPosition(self, N):
        # code here 
        a = bin(N).replace('0b','')
        
        k = a[::-1].find('1')
        
        if(a.count('1')==1):
            return k+1
        
        return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.findPosition(N))
# } Driver Code Ends