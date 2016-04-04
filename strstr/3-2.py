# time 15 mins
# used time 15 mins

# time 15 mins
# used time 15 mins

# this is actually a correct solution
# the code i submitted a day ago, which passed lintcode, is actually wrong after i looked KMP up
# the previous version does not take care of the situations where the target contains repeatitive elements

class Solution:
    def strStr(self, source, target):
        
        ## try O(n) with no bug
        
        if source is None or target is None: 
            return -1
        
        source_pointer = 0
        target_pointer = 0
        
        last_target_begining_match = None
        
        while source_pointer < len(source):
            if target_pointer == len(target):
                return source_pointer - len(target)
            
            if source[source_pointer] == target[target_pointer]:
                if target_pointer != 0 and target[target_pointer] == target[0] and last_target_begining_match is None:
                    last_target_begining_match = target_pointer
                target_pointer += 1
            else:
                if last_target_begining_match is not None:
                    target_pointer = last_target_begining_match + 1
                    last_target_begining_match = None
                elif source[source_pointer] == target[0]:
                    target_pointer = 1
                else:
                    target_pointer = 0
                
            source_pointer += 1
        else:
            if target_pointer == len(target):
                return source_pointer - len(target)
            return -1
