# time 30mins
# cost 17 mins
# iteration
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # do it without recursion
        
        if not nums:
            return []
            
        if len(nums) == 1:
            return [nums]
        
        all_permutations = [[]]
        for i in nums:
            permutations = []
            for permutation in all_permutations:
                for k in range(len(permutation) + 1):
                    permutations.append(permutation[0:k] + [i] + permutation[k:])
            all_permutations = permutations
        return all_permutations

# wrong time complexity
