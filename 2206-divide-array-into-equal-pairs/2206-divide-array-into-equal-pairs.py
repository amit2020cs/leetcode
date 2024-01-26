class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] =1
        for k, v in hashmap.items():
            if v % 2 != 0:
                return False
        return True