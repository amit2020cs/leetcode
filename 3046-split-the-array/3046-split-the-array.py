class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        dic = {}
        
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for key, value in dic.items():
            if value>2:
                return False
        return True