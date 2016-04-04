# time: 15 mins
# tried O(n**2), but encountered a bug which took me 10 mins to debug =(

class Solution:
    def strStr(self, source, target):
        
        ## try O(n**2) solution
        ## time - around 20 mins
        
        if source is None or target is None:
            return -1
        
        
        if len(target) > len(source):
            return -1
        if len(target) == len(source):
            for i in range(len(target)):
                if source[i] != target[i]:
                    return -1
                else:
                    return 0
        
        # when target length < source length
        for i in range(len(source) - len(target) + 1):
            for k in range(len(target)):
                if source[i + k] != target[k]:
                    break
            else:
                return i
            i += 1
        else:
            return -1
                
        
        
        
        
