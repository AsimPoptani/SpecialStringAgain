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