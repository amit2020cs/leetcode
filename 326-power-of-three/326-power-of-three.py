class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n > 0:
        #     if log(n, 3) % 1 == 0:
        #         return True
        #     else:
        #         return False
        return n>0 and (3**19)%n==0