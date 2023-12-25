class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]
        
        import heapq
        priority_queue = nums[:k]
        
        heapq.heapify(priority_queue) #this will place the smallest element of the array at zeroth position.
        
        for x in nums[k:]:
            heapq.heappush(priority_queue, x)#this line will push the element x in the heap which we made
            
            heapq.heappop(priority_queue) 
            #this line will pop the zeroth element from the array.
        
        return priority_queue[0]
        
        