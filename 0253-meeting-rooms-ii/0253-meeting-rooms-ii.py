class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        
        start = sorted([i[0] for i in intervals])
        end = sorted(i[1] for i in intervals)
        i = 0 
        j = 0
        croom = 0
        oroom = 0
        
        while i< n:
            if start[i] < end[j]:
                croom+=1
                i+=1
            else:
                croom-=1
                j+=1
            oroom = max(oroom, croom)
        
        return oroom