#User function Template for python3

class Solution:
    def increment(self, arr, N):
        # code here 
        if arr[N-1]==9:
            int1=''
            for t in arr:
                int1+=str(t)
            return str(int(int1)+1)
        for t in range(0,9):
            arr[N-1]+=1
            return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
# } Driver Code Ends