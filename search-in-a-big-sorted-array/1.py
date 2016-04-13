# time 30
# left 11:55
# iterative

"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # if there is no number on that index, return -1
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader 
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        
        if reader is None or reader.get(0) == -1:
            return -1 
            
        if target <= 0:
            return -1
        
        
        # finds the upper bound
        start = 0
        end = 1 
        
        while not (reader.get(end) == -1 or reader.get(end) > target):
            end *= 2
        
        # get an end that is either the end or a number that is greater or equal than target
        mid = start - (start - end) / 2
        
        while start + 1 < end:
            if reader.get(mid) == -1:
                end = mid
            elif reader.get(mid) > target:
                end = mid
            elif reader.get(mid) < target:
                start = mid
            elif reader.get(mid) == target:
                end = mid
            mid = start - (start - end) / 2
        
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
        
