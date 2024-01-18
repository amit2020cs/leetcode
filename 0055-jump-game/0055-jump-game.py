class Solution:
    def canJump(self, num: List[int]) -> bool:
        goal = len(num) -1
        
        for i in range(goal-1,-1,-1):
            if i + num[i] >= goal:
                goal = i
        return True if goal==0 else False
        