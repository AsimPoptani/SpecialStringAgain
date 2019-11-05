def substring_checker(in_str):
    # All same?
    if len(set(in_str)) == 1:
        return True
        
    # All same except middle?
    else:
        in_list = list(in_str)
        if len(in_list) % 2 == 1:
            del in_list[len(in_list) // 2]
            if len(set(in_list)) == 1:
                return True
            else:
                return False
        else:
            return False

def calc_substring(string):
    total=0
    for index in range(1,len(string)+1):
        head=index
        tail=0
        while (head != len(string)+1):
            if substring_checker(string[tail:head]): # insert function here
                total+=1
            tail+=1
            head+=1
    return total

exampleString ="abcbaba"
print(calc_substring(exampleString))
