class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = []
        
        for i , j in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < j:
                prev_day = stack.pop()
                
                res[prev_day] = i - prev_day
            stack.append(i)
            
        return res
        