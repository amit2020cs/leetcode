class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        hashmap = {}
        
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        n = len(nums)
        
        for key, value in hashmap.items():
            if value> n//2 and key== target:
                return True
        return False
        