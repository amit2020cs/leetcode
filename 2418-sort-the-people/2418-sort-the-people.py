class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         _,names = zip(*sorted(zip(heights,names), reverse = True)) 
        
#         return list(names)
        res = []
        for i in range(len(names)):
            res.append([heights[i],names[i]])
        res = sorted(res,reverse=True)
        return [name for height,name in res]