# time: 30 mins
# cost time: ~ 12 mins left

# runtime? sort + ops
# sort = log(N)
# + 2^O(N) * 2*O(N)
# == 2 ^ O(N)
# is there a better way?
# how to do this in recursion???

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        subsets = []
        
        # len(S) = 3
        # 000 001 010 etc.
        # 2 ^ 3 
        S.sort()
        for i in range(2 ** len(S)):
            this_set = []
            for k in range(len(S)):
                if (i / (2 ** k)) % 2:
                    this_set.append(S[k])
            subsets.append(this_set)
        return subsets
    
