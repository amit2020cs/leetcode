class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # lo,hi = 0, len(letters)-1

        # while hi>lo:
        #     mid = lo+(hi-lo)//2
        #     if letters[mid]<=target:
        #         lo = mid+1
        #     else:
        #         hi = mid-1
        # if letters[hi] <= target:
        #     return letters[hi]
        # else:
        #     return letters[hi-1]

        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]