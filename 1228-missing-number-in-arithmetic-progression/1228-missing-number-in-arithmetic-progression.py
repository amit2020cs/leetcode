class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        return int((arr[-1] + arr[0])/2 * ( n+1) -sum(arr))
        
        