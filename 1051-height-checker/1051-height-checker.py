class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = sorted(heights)
        count = 0
        for i in range(0,len(heights)):
            if res[i]==heights[i]:
                pass
            else:
                count+=1
        return count
        