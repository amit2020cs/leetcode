class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        hashmap = {}
        
        for i in arr:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        
        frequency = list(hashmap.values())
        
        frequency.sort()
        ele_removed = 0
        for i in range(len(frequency)):
            
            ele_removed += frequency[i]
            
            if ele_removed > k:
                return len(frequency) - i
        
        return 0
            