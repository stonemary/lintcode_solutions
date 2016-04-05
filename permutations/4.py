# time 30mins
# cost time - 9mins

# recursive

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # try recursive?
        
        if nums is None or nums == []:
            return []
        if len(nums) == 1:
            return [nums]
            
        total_permutation = []
        for permutation in self.permute(nums[1:]):
            for i in range(len(permutation) + 1):
                total_permutation.append(permutation[0:i] + [nums[0]] + permutation[i:])
        return total_permutation

# time complexity:
# (N-1) * (N-1)! + (N-2)*(N-2)! + ... + N-(N-1)(N-(N-1))! = N! -1

# test case found bug: 
# 1. case [] lost
# 2. lost [nums[0]]'s outer [ ]
