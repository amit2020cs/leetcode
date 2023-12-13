class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l = sorted(nums)
        # result = []
        count=0
        i = 0
        j = len(l)-1
        while(i<j):
            if l[i]+l[j]==k:
                # result.append((l[i],l[j]))
                # l.remove(l[i])
                # l.remove(l[j])
                count+=1
                i+=1
                j=j-1
            elif l[i]+l[j]>k:
                j=j-1
            else:
                i=i+1
        return count
        