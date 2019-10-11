#print a list in reverse using recursion

def print_in_reverse(listt,length):
    if length<1:
        return 0
    print(listt[length-1]),
    print_in_reverse(listt,length-1)


