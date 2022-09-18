class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        A = nums[0:n]
        B = nums[n:]
        A.reverse()
        B.reverse()
        
        l = []
        for i in range(len(nums)):
            if i%2==0:
                l.append(A.pop())
            else:
                l.append(B.pop())
        return l