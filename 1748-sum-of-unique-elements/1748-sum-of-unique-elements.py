class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # dic = {}
        # for i in nums:
        #     if i not in dic:
        #         dic[i]=1
        #     else:
        #         dic[i]+=1
        # result = 0
        # for key, val in dic.items():
        #     if val == 1:
        #         result += key
        # return result       
        return sum([number for number, count in Counter(nums).items() if count == 1])