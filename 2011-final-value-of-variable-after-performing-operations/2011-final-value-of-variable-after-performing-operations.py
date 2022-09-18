class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dt = {"X++":1,"++X":1,"--X":-1,"X--":-1}
        x = 0
        for ele in operations:
            x +=dt[ele]
        return x
        