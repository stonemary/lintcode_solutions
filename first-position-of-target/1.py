# time 15mins
# cost 8 mins
# recursive
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        
        # recursive
        if nums is None or nums == []:
            return -1
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        
        mid = len(nums) / 2
        
        if nums[mid] == target:
            # need to gurantee it's the first one...
            while nums[mid] == target:
                mid -= 1
            return mid + 1
        if nums[mid] < target:
            result = self.binarySearch(nums[mid:], target)
            if result == -1:
                return result
            return mid + result
        else:
            return self.binarySearch(nums[:mid], target)
        
