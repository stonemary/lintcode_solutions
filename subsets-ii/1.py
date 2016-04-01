# time: 30 mins
# time cost: 21 mins

# not best solution, still 2 ** O(N)

class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        
        subsets = []
        S.sort()
        full_hash = {}
        for i in range(2 ** len(S)):
            this_set = []
            this_string = ''
            for k in range(len(S)):
                if (i / (2 ** k)) % 2:
                    this_set.append(S[k])
                    this_string += str(S[k])
            # most stupid way: find 
            # worst run time:
            # 1 + 2 + ... + 2**O(N) = (2**O(N))**2 = 2**2O(N) =_= worse..
            # ha, can we use a dictionary???
            # how to find out if two lists are the same?
            # string?
            # 2**O(N) storage, 2**O(N) time..
            if not full_hash.get(this_string):
                subsets.append(this_set)
                full_hash[this_string] = this_set
        return subsets
