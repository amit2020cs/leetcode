class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
                
        arr.sort()
        min_abs_diff = float('inf')
        answer=[]
        for i in range(len(arr) -1 ):
            min_abs_diff = min(min_abs_diff,arr[i+1] - arr[i])
            
        for i in range(len(arr) - 1):   
            if arr[i + 1] - arr[i] == min_abs_diff:
                answer.append([arr[i], arr[i + 1]])
        return answer
            
        