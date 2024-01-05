class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        
        if n==0: return 0
        k = len(costs[0])
        
        for h in range(1,n):
            
            for c in range(k):
                
                best = math.inf
                
                for p in range(k):
                    
                    if c == p: continue
                    
                    best = min(best, costs[h-1][p])
                costs[h][c]+=best
                
        return min(costs[-1])