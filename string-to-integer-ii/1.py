# time: 45 mins
# cost time: 1:10 over time, but did have a partial solution @45mins

# the question is not clear, it reads like python int, but it's actually perl int
# run time: O(N) but very complicated, look at ways to simply this - maybe do some preprocessing rather than do it all in one shot

class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, string):
        string_pointer = 0
        integer = 0
        
        zero = 0
        
        max_length = 10
        reach_max = False
        
        signs = {
            '+': 1,
            '-': -1
        }
        dot = '.'
        INT_MAX = 2147483647
        INT_MIN = 2147483648
        sign = None
        sign_index = None
        point_count = 0
        point_index = None
        
        see_first_digit = False
        see_last_digit = False
        
        integer_length = 0
        max_index = None
        
        digit_map = {str(i): i for i in range(10)}


        while string_pointer < len(string):
            
            if string[string_pointer] not in digit_map.keys():
                if string[string_pointer] == ' ':
                    if see_first_digit:
                        see_last_digit = True
                elif string[string_pointer] == dot:
                    if not see_first_digit:
                        return zero
                    elif see_last_digit:
                        break
                    elif string[string_pointer - 1] not in digit_map.keys():
                        break
                    elif point_count:
                        break
                    else:
                        point_count += 1
                        # make sure there are digits after the dot
                        point_index = string_pointer
                elif string[string_pointer] in signs.keys():
                    if sign is not None:
                        break
                    if see_first_digit:
                        break
                    else:
                        see_first_digit = True
                        sign = signs[string[string_pointer]]
                        sign_index = string_pointer
                else:
                    break
            else:
                if not see_first_digit:
                    see_first_digit = True
                
                if see_last_digit:
                    break
                
                if point_count:
                    break
                else:
                    integer = integer * 10 + digit_map[string[string_pointer]]
                    see_first_digit = True
                    integer_length += 1
                    if integer_length == max_length:
                        reach_max = True
                        max_index = string_pointer
                        break

            string_pointer += 1
        else:
            # no numbers after the dot
            if point_count and string_pointer == point_index + 1:
                return zero
            # no numbers after the sign
            if sign is not None and string_pointer == sign_index + 1:
                return zero
            
        # reaches the max number of digits
        if reach_max:
            if (max_index + 1 == len(string)) or string[max_index + 1] == dot:
                if sign is None or sign == 1:
                    if str(integer) > INT_MAX:
                        integer = INT_MAX
                else:
                    if str(integer) > INT_MIN:
                        integer = INT_MIN
            else:
                if sign is None or sign == 1:
                    integer = INT_MAX
                else:
                    integer = INT_MIN
            
        if sign is not None:
            integer *= sign
        
        return integer

