class Solution:
    def confusingNumber(self, n: int) -> bool:
        m = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        n = str(n)
        l = len(n)
        diff = 0
        for i in range(l):
            if n[i] not in m:
                return False
            diff |= m[n[i]] != n[l-i-1]
        return diff != 0