class Solution:
    def reformatDate(self, date: str) -> str:
        M = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        d, m, y = date.split() 
        return f'{y}-{(M.index(m)+1):02d}-{int(d[:-2]):02d}'
        