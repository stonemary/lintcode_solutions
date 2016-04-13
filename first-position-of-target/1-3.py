# time 15
# 2:40
# improvement on the last version: prevent overflow
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        
        # iterative
        if nums is None or nums == []:
            return -1
        
        start = 0
        end = len(nums) - 1
        mid = (start + end) / 2
        last_mid = None
        
        while start + 1 < end:
            # for first item
            if nums[mid] == target:
                last_mid = mid
                end = mid
            if nums[mid] < target: 
                start = mid
            if nums[mid] > target:
                end = mid
            # overflow prevention
            mid = start - (start - end) / 2
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
            
                
        
