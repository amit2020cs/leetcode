class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i]=1
        sorted_items = sorted(hashmap.items(), key= lambda x: x[1] , reverse = True)
        res = "".join([char * freq for char, freq in sorted_items])
        
        return res