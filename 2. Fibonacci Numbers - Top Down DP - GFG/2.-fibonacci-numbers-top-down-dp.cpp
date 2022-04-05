// { Driver Code Starts
//Initial Template for C++


#include <bits/stdc++.h>
#include <fstream>
using namespace std;



 // } Driver Code Ends
//User function Template for C++

//Complete this function
class Solution
{
    public:
    //Function to find the nth fibonacci number using top-down approach.
    long long findNthFibonacci(int n, long long int dp[])
    {
        // Your Code Here
        if(n==0 || n== 1) {
            return dp[n]=n; 
        }

        if(dp[n]!=0){
            return dp[n];
        }
        long fibm1 = findNthFibonacci(n-1,dp);
        long fibm2 = findNthFibonacci(n-2,dp);

        long fibn = fibm1 + fibm2;
        return dp[n]=fibn;
    }

};

// { Driver Code Starts.

int main()
 {
    //initializing base value
    long long dp[100]={0};
    dp[0]=0;
    dp[1]=1;
    dp[2]=1;
    
    //taking total testcases
    int testcases;
    cin>>testcases;
    
    while(testcases--)
    {
        //taking nth number 
        int number;
        cin>>number;
        
        //calling findNthFibonacci() function
        Solution obj;
        cout<<obj.findNthFibonacci(number, dp)<<endl;
    }
    
	return 0;
}
  // } Driver Code Ends