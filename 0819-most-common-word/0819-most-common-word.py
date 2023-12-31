class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = normalized_str.split()
        dic = defaultdict(int)
        banned_words = set(banned)
        for i in words:
            if i not in banned_words:
                dic[i] += 1
        return max(dic.items(),key=operator.itemgetter(1)) [0]
                
                
            
        
        