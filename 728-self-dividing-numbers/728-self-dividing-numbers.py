class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        
        for i in range(left, right+1):
            for dig in str(i):
                if int(dig) ==0 or i % int(dig)!=0:
                    break
            else:
                res.append(i)
        return res
#         result = []
#         for num in range(left, right + 1):
#             for dg in str(num):
#                 if int(dg) == 0 or num % int(dg) != 0:
#                     break
#             else:
#                 result.append(num)
        
#         return result

            
        