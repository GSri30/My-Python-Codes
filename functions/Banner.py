#Write a function banner(m) that prints prints the message m decorated with borders. For
#example, banner("Good Morning!") with give:

# *** ****** ****** **
# * _Good Morning ! _*
# *** ****** ****** **

def banner(m):
    l=len(m)
    #for the first line design
    print("*" * (l+4))
    #for the line containing the message
    print("* " + m + " *")
    #for the last line design
    print("*" * (l+4))

banner()

