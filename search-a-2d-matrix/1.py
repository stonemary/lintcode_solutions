# iterative
# time: over time, bug on helper function. ~ 18mins

class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if matrix is None or matrix == []:
            return False
            
        # width: m, height: n
        n = len(matrix)
        m = len(matrix[0])
        start = 0
        end = m * n - 1
        mid = (start + end) / 2
        
        while start + 1 < end:
            mid_value = self.get_element(matrix, mid, m)
            if mid_value == target:
                return True
            if mid_value < target:
                start = mid
            if mid_value > target:
                end = mid
            mid = (start + end) / 2
        else:
            if self.get_element(matrix, start, m) == target:
                return True
            if self.get_element(matrix, end, m) == target:
                return True
            return False
            
            
    
    def get_element(self, matrix, i, m):
        index_1 = i / m 
        index_2 = i % m
        return matrix[index_1][index_2]
