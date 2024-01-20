class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {char: idx for idx, char in enumerate(keyboard)}
        total_time = prior_idx = 0
        for char in word:
            idx = d[char]
            total_time += abs(idx - prior_idx)
            prior_idx = idx
        return total_time
        