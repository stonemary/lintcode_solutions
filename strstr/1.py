# time 15 mins
class Solution:
    def strStr(self, source, target):
        
        if source is None or target is None:
            return -1 
        
        source_index = 0
        target_index = 0
        
        while source_index != len(source):
            
            # found
            if target_index == len(target):
                return source_index - len(target)
            
            # operations
            if source[source_index] == target[target_index]:
                target_index += 1
            elif source[source_index] == target[0]:
                target_index = 1
            else:
                target_index = 0
        
            # next
            source_index += 1
            
        else:
            if target_index == len(target):
                return source_index - len(target)
            return -1
