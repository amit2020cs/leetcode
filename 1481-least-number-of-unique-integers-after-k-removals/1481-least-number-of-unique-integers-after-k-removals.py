class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        frequency_map = Counter(arr)
        frequency = list(frequency_map.values())
        frequency.sort()
        ele_removed = 0
        for i in range(len(frequency)):
            
            ele_removed += frequency[i]
            
            if ele_removed > k:
                return len(frequency) - i
        
        return 0
            