class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        
        N = len(arr)+1
        n = int(0.05*N)
        
        return mean(arr[n : len(arr) - n])
            