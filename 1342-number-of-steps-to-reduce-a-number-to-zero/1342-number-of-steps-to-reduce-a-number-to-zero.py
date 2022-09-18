class Solution:
    def numberOfSteps(self, num: int) -> int:
        count  = 0
        n = num
        while n>0:
            if n%2==0 and n is not 0:
                n/=2
                count+=1
            if n%2==1 and n is not 0:
                n-=1
                count+=1
        return count
        
        
        