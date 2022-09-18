class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        for i in sentences:
            curr_result = i.count(" ")+1
            if curr_result > result:
                result = curr_result
        return result