# time 45 mins
# cost time: ~ 45 mins

# this should be python int... but it takes care of the leading/tailing spaces etc. not sure if it works or not

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
                        return zero
                    elif string[string_pointer - 1] not in digit_map.keys():
                        return zero
                    elif point_count:
                        return zero
                    else:
                        point_count += 1
                        # make sure there are digits after the dot
                        point_index = string_pointer
                elif string[string_pointer] in signs.keys():
                    if sign is not None:
                        return zero
                    if see_first_digit:
                        return zero
                    else:
                        see_first_digit = True
                        sign = signs[string[string_pointer]]
                        sign_index = string_pointer
                else:
                    return zero
            else:
                if not see_first_digit:
                    see_first_digit = True
                
                if see_last_digit:
                    return zero
                
                if point_count or reach_max:
                    pass
                else:
                    integer = integer * 10 + digit_map[string[string_pointer]]
                    see_first_digit = True
                    integer_length += 1
                    if integer_length == max_length:
                        reach_max = True
                        max_index = string_pointer

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
                if string[max_index + 1] == dot:
                    if string(integer) > str(INT_MAX):
                        integer = INT_MAX
                else:
                    integer = INT_MAX
            
            if sign is not None:
                integer *= sign
                
            return integer
        
