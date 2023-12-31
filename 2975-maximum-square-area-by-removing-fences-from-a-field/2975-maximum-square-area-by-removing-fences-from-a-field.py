class Solution:
    def maximizeSquareArea(self, M: int, N: int, H: List[int], V: List[int]) -> int:
        MOD = 10 ** 9 + 7
        H.append(M)
        H.append(1)
        V.append(N)
        V.append(1)
        H.sort()
        V.sort()
        HH = set()
        for i in range(len(H)):
            for j in range(i + 1, len(H)):
                HH.add(H[j] - H[i])
        VV = set()
        for i in range(len(V)):
            for j in range(i + 1, len(V)):
                VV.add(V[j] - V[i])
        s = HH & VV
        if not s:
            return -1
        res = max(s)
        return res * res % MOD
