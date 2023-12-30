class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(tuple(x) for x in grid)
        return sum(rows[tuple(x)] for x in zip(*grid))