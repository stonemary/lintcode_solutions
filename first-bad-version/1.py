# time 30
# left 17
#classSVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can useSVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        
        start = 1
        end = n
        mid = start - (start - end) / 2
        
        while start + 1 < end:
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid
            mid = start - (start - end) / 2
        
        if SVNRepo.isBadVersion(start):
            return start
        if SVNRepo.isBadVersion(end):
            return end
        
