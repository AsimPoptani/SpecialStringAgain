


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

exampleString ="aabaa"
calc_substring(exampleString)