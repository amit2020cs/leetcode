#User function Template for python3
class Solution:
    def maximumSumSubarray (self,k,arr,N):
        # code here 
        max_sum, window_sum = 0, 0
        window_start = 0
    
        for window_end in range(len(arr)):
            window_sum += arr[window_end]  # add the next element
            # slide the window, no need to slide if we've not hit the required window size of 'k'
            if window_end >= k-1:
                max_sum = max(max_sum, window_sum)
                window_sum -= arr[window_start]  # subtract the element going out
                window_start += 1  # slide the window ahead
        return max_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends