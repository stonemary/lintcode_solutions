# time 30mins
# cost: 22 mins
# actually i was thinking of it in shower, so takes more time than recorded

class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        
        # recursive
        
        S.sort()
        first, last = self.subsets_recursion_helper(S)
        return first + last
        
    def subsets_recursion_helper(self, S):
        
        if S is None:
            return [], []
        if S == []:
            return [], [[]]
        if len(S) == 1:
            return [[]], [S]
        
        these_subsets = []
        first, last = self.subsets_recursion_helper(S[:-1])
        
        if S[-1] != last[-1][-1]:
            for subset in first + last:
                these_subsets.append(subset + [S[-1]])
        else:
            for subset in last:
                these_subsets.append(subset + [S[-1]])
        
        return first + last, these_subsets
        
# the key here is that you would need to remember your last operation
# run time: Nlog(N) + 2**(N-1) + 2**(N-2) + ...... + 2**0 = O(2**N)       
