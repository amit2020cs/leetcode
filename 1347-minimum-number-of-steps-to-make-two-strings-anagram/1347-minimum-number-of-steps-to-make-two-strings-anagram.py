class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = [0] *26
        count_t = [0] *26
        
        for i in s:
            count_s[ord(i) - ord('a')]+=1
        for j in t:
            count_t[ord(j) - ord('a')] +=1
            
        result = 0
        for i in range(26):
            if count_s[i] > count_t[i]:
                result += count_s[i] - count_t[i]
        return result
            
        