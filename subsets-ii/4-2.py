# time: 30mins
# cost time: ~30mins

# iterative
class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        
        if S is None:
            return []
        if S == []:
            return [[]]
            
        
        S.sort()
        last_sets = []
        new_sets = [[]]
        for i in S:
            these_sets = []
            if new_sets[-1] == [] or new_sets[-1][-1] != i:
                for subset in last_sets + new_sets:
                    these_sets.append(subset +[i])
            else:
                for subset in new_sets:
                    these_sets.append(subset + [i])
            last_sets = last_sets + new_sets
            new_sets = these_sets
            these_sets = []
        return last_sets + new_sets

# run time:
# nlog(n) + 2**0 + 2**1 + 2**2 + ... + 2**(N-1) = 2 ** N
