class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] = 1
        
#         for i in range(len(nums)):
#             if nums[i] in hashmap:
#                 hashmap[nums[i]] += 1
#             else:
#                 hashmap[nums[i]] = 1

        
        
        # Sort the dictionary items based on frequency in descending order
        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        
        # Extract the keys (numbers) from the sorted items
        res = [x[0] for x in sorted_items]
        
        return res[:k]

            
        