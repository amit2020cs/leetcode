class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         hashmap = {}
        
#         for i in range(len(nums)):
#             if nums[i] in hashmap:
#                 hashmap[nums[i]]+=1
#             hashmap[nums[i]]=1
        
#         res = [x for x in sorted(hashmap.values(), reverse=True)]
#         return res[:k]
        
        return [x for x, y in collections.Counter(nums).most_common(k)]
        
            
        