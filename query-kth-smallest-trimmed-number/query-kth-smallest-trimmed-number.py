class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        def counting_sort(arr, key):
            d = {k: [] for k in range(10)}
            for n in arr:
                d[key(n)] += n,
            return sum(d.values(), [])

        search, idx = {}, list(range(len(nums)))

        for i in range(1, len(nums[0]) + 1):
            fn = lambda n: int(nums[n][-i])
            idx = counting_sort(idx, fn)
            search[i] = idx

        return [search[i][k - 1] for k, i in queries]