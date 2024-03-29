class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i +1
            else:
                return map[num[i]], i+1

        return -1, -1