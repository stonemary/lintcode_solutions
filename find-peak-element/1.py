# 30
# l 15
class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        
        if A is None or len(A) <= 2:
            return 0
            
        if len(A) == 3:
            return 1
            
        start = 0
        end = len(A) - 1
        mid = start - (start - end) / 2
        
        while start + 2 < end:
            
            # if mid is going up
            if A[mid - 1] < A[mid] < A[mid + 1]:
                start = mid
            
            elif A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
            
            elif A[mid - 1] > A[mid] > A[mid + 1]:
                end = mid
            
            else:
                end = mid
                
            mid = start - (start - end) / 2
            
        return start + 1
