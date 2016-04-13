class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        
        if A is None or A == []:
            return 0
            
        start = 0
        end = len(A) - 1
        # this is actually mid = start + (end - start) / 2
        mid = (start + end) / 2
        
        while start + 1 < end:
            if A[mid] < target:
                start = mid
            elif A[mid] == target:
                return mid
            else:
                end = mid
            mid = (start + end) / 2
        else:
            if A[start] >= target:
                return start
            if A[end] >= target: 
                return end
            if A[end] < target:
                return end + 1
        

