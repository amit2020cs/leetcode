class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for row in image:
            result.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
        return result