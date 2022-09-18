class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = []
        y = []
        z = []
        for i in nums[:n]:
            x.append(i)       
        for j in nums[n:]:
            y.append(j)
        for i,j in zip(x,y):
            z.append(i)
            z.append(j)
        return z