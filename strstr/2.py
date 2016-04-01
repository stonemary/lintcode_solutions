# 15 mins
class Solution:
    def strStr(self, source, target):
        
        source_pointer = 0
        target_pointer = 0
        
        if source is None or target is None:
            return -1
        
        while source_pointer < len(source):
            
            if target_pointer == len(target):
                return source_pointer - len(target)
                
            if source[source_pointer] == target[target_pointer]:
                target_pointer += 1
            elif source[source_pointer] == target[0]:
                target_pointer = 1
                
            else:
                target_pointer = 0
            source_pointer += 1
        else:
            if target_pointer == len(target):
                return source_pointer - len(target)
            return -1
