class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for x in nums: 
            if x > 0: pos.append(x)
            else: neg.append(x)
        ans = []
        for p, n in zip(pos, neg): ans.extend([p, n])
        return ans