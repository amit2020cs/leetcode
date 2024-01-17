class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}

        for i in arr:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        seen = set()
        for _, count in dic.items():
            if count in seen:
                return False
            seen.add(count)
        return True
        