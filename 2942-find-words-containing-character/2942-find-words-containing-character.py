class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        
        for i, k in enumerate(words):
            if x in k:
                res.append(i)
        return res
        