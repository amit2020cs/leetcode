class Solution:
    def arraySign(self, nums: List[int]) -> int:
#         if 0 in nums:
#             return 0
        
#         hashmap = {"pos":0}
        
#         for i in nums:
#             if i<0:
#                 hashmap["pos"]+=1
            
#         neg_count = int(hashmap.values())
        
#         if neg_count%2==0:
#             return 1
#         return -1

        if 0 in nums:
            return 0

        neg_count = sum(1 for i in nums if i < 0)

        return 1 if neg_count % 2 == 0 else -1