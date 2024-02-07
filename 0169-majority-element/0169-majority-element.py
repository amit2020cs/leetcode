class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashmap = {}
        
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        n = len(nums)
        
        for key, value in hashmap.items():
            if value> n//2:
                return key
            
                
        