# time: 30 mins
# used time: 8 mins
# this time try use recursion to solve the problem

# thought: every element can be in a set or not; if i know all subsets from S[:-1], i can know all subsets from S

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # implement it recursively
        
        if S is None:
            return []
        if S is []:
            return []
        
        if len(S) == 1:
            return [[], S]
        
        # recursive
        S.sort()
        
        # non-descending.. 
        all_sets = []
        for subset in self.subsets(S[:-1]):
            all_sets.append(subset + [S[-1]])
            all_sets.append(subset)
        return all_sets

# runtime: 
# sort: nlog(n),
# each f(N) with a sort of nlog(N) + O((N-1)**2) = O(N**2) and there are N of them so O(1**2) + O(2**2) + .. O((N-1)**2) = N*(N**2)/2 = N**3 ?
