class Solution:
    def isPalindrome(self, x: int) -> bool:
        # reversed_num = 0
        # while x != 0:
        #     digit = x % 10
        #     reversed_num = reversed_num * 10 + digit
        #     x //= 10
        # if x==reversed_num:
        #     return True
        # else:
        #     return False
        return str(x) == str(x)[::-1]