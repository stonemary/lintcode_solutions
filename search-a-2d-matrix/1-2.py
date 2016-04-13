# time 15mins
# cost: 20min~
# use recursion
class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        
        # recursion
        if matrix is None or matrix == []:
            return False
            
        if len(matrix) == 1:
            #print('enter 1 row: {}'.format(matrix))
            if matrix[0] is None or matrix[0] == []:
                return False
            if len(matrix[0]) == 1:
                if matrix[0][0] == target:
                    return True
                else:
                    return False
                
            mid = len(matrix[0]) / 2
            if matrix[0][mid] == target:
                return True
            if matrix[0][mid] < target:
                return self.searchMatrix([matrix[0][mid:]], target)
            else:
                return self.searchMatrix([matrix[0][:mid]], target) 
        
        mid = len(matrix) / 2
        if matrix[mid][0] == target:
            return True
        if matrix[mid][0] > target:
            return self.searchMatrix(matrix[:mid], target)
        else:
            return self.searchMatrix(matrix[mid:], target)
        
        
