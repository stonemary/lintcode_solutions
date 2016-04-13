# recursion
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        
        if A is None or A == []:
            return 0
            
        if len(A) == 1:
            if A[0] == target:
                return 0
            if A[0] > target:
                return 0
            if A[0] < target:
                return 1
        
        
        start = 0
        end = len(A)
        mid = (start + end) / 2
        
        
        if A[mid] < target:
            return mid + self.searchInsert(A[mid:end], target)
        if A[mid] == target:
            return mid
        if A[mid] > target:
            return self.searchInsert(A[start:mid], target)
        
        
        

