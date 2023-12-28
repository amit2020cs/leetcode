class Solution:
    def subarraySum(self, nums, k):
        count = curr_sum = 0
        h = defaultdict(int)
        
        for num in nums:
            # The current prefix sum
            curr_sum += num
            
            # Situation 1:
            # Continuous subarray starts 
            # from the beginning of the array
            if curr_sum == k:
                count += 1
            
            # Situation 2:
            # The number of times the curr_sum − k has occurred already, 
            # determines the number of times a subarray with sum k 
            # has occurred up to the current index
            count += h[curr_sum - k]
            
            # Add the current sum
            h[curr_sum] += 1
                
        return count