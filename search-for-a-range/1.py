# 30
# l 7
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if A is None or A == []:
            return [-1, -1]
            
        start = 0
        end = len(A) - 1
        mid = start - (start - end) / 2
        
        while start + 1 < end:
            if A[mid] > target:
                end = mid
            if A[mid] < target:
                start = mid
            if A[mid] == target:
                break
            mid = start - (start - end) / 2
        else:
            if A[start] == target:
                if A[end] == target:
                    return [start, end]
                if A[end] != target:
                    return [start, start]
            else:
                if A[end] == target:
                    return [end, end]
                else:
                    return [-1, -1]
                    
        new_end = new_start = mid
        # find start
        mid = start - (start - new_end) / 2
        while start + 1 < new_end:
            if A[mid] >= target:
                new_end = mid
            if A[mid] < target:
                start = mid
            mid = start - (start - new_end) / 2
            
        if A[start] != target:
            start = new_end
        
        # find end
        mid = new_start - (new_start - end) / 2
        while new_start + 1 < end:
            if A[mid] <= target:
                new_start = mid
            else:
                end = mid
            mid = new_start - (new_start - end) / 2
        if A[end] != target:
            end = new_start
        return [start, end]
        
        
        
