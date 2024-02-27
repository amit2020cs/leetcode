class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for i in operations:
            if i.isdigit() or (i[0] == '-' and i[1:].isdigit()):
                res.append(int(i))
            elif i == 'C':
                res.pop()
            elif i == 'D':
                res.append(res[-1] * 2)
            elif i == '+':
                res.append(res[-1] + res[-2])

        return sum(res)