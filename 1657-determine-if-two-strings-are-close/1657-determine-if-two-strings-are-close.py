class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        feq1 = Counter(word1)
        feq2 = Counter(word2)
        
        if set(feq1.keys()) != set(feq2.keys()):
            return False
        feq1 = dict(sorted(feq1.items(), key= lambda item: item[1]))
        feq2 = dict(sorted(feq2.items(), key= lambda item: item[1]))
        return [feq for feq in feq1.values()] == [feq for feq in feq2.values()]       