class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(0,n):
            j = n-1-i
            
            if j==n-1:
                prev = arr[j]
                arr[j] = -1
            else:
                temp = arr[j]
                arr[j] = prev
                
                if temp > prev:
                    prev  = temp
        return arr
                
            
                       
                       
                       
            