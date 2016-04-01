# time: 30 mins
# time cost: 17 mins
# bad solution: N stack, each with O(N!) space, time: sum n->N [O(n) * O((n-1)!)] = sum n->N [O(n!)] oh crap

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        # numbers of permutation:
        # N * N-1 * ... * 1 = N!
        
        # recursion
        if nums is None:
            return []
            
        if nums == []:
            return []
        
        if len(nums) == 1:
            return [nums]
        
        if len(nums) > 1:
            this_permutation = []
            # bad: this is factorial N...ORZ
            # number of stack: O(N)
            digit = nums[0]
            last_permutation = self.permute(nums[1:])
            
            for item in last_permutation:
                for i in range(len(item) + 1):
                    new_item = item[:i] + [digit] + item[i:]
                    this_permutation.append(new_item)
            return this_permutation
                
                
        
            
