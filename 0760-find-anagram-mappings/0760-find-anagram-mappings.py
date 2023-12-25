class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        
        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j]:
                    res.append(j)
                    break
        return res
        