# time 30 mins
# cost time: 10 mins

# actually took me sometime to think ..
class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # implement it iteratively
        # there are: 
        # 2**N subsets, because either number can decide whether it goes into a subset or not
        
        all_subsets = [[]]
        # needs to sort
        S.sort()
        for i in S:
            temp_sets = []
            for subset in all_subsets:
                temp_sets.append(subset + [i])
            all_subsets += temp_sets
            
        return all_subsets

# time complexity:
# sort nlog(n)
# for loop: N * 2^0 + (N-1)*2^1 + ... + N*2^(N-1) = 2**(N+1) - 2 - N (大神告诉我这个是等于这个的ORZ,所以这是什么鬼complexity!) 
