class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        if num < 0:
            num = 2**32 + num  # Convert negative number to its two's complement representation

        hex_chars = "0123456789abcdef"
        result = ''

        while num > 0:
            remainder = num % 16
            result = hex_chars[remainder] + result
            num //= 16

        return result
