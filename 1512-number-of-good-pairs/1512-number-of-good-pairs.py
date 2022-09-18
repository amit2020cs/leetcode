class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair_dict = {}
        pairs = 0
        for i in nums:
            try:
                pair_dict[i]+=1
                pairs += pair_dict[i] -1
            except:
                pair_dict[i] = 1
        return pairs
        