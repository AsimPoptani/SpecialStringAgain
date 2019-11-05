import collections

s_set = collections.defaultdict(int)


def substring_checker(in_str):
    # All same?
    if len(set(in_str)) == 1:
        print("found special", in_str)
        return True
        
    # All same except middle?
    else:
        in_list = list(in_str)
        if len(in_list) % 2 == 1:
            del in_list[len(in_list) // 2]
            if len(set(in_list)) == 1:
                print("found special", in_str)
                return True
            else:
                return False
        else:
            return False

def calc_substring(string):
    if len(string) == 1:
        return 1
    elif string in s_set.keys():
        return s_set[string]
    else:
        # Not in, calculate
        if substring_checker(string):
            value = 1 + calc_substring(string[0:len(string)-1]) + calc_substring(string[1:len(string)])
            s_set[string] = value
            return value
        else:
            value = calc_substring(string[0:len(string)-1]) + calc_substring(string[1:len(string)])
            s_set[string] = value
            return value


exampleString ="mnonopoo"
print(calc_substring(exampleString))
