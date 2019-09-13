#Write a function ndiamond(n) that prints a numerical diamond of height n. For example,
#ndiamond(3) will give:

#_1
#121
#_1

def ndiamond(n):
    #first half of the pattern
    #go to each line
    for i in range(n-1):
	#print specific number of spaces (depending upon the value of i)
        for j in range(n-i-2):
            print("\b "),
	#print the specific accending numbers in same line
        for k in range(1,i+2):
            print("\b"+str(k)),
	#print the specific descending numbers in same line
        for l in range(i,0,-1):
            print("\b"+str(l)),
	#go to next line
        print(" ")
    #reset the values
    i=9
    j=0
    k=0
    l=0
    #second half of the pattern 
    #simillarly print in reverse order
    for i in range(n-2):
        for j in range(i+1):
            print("\b "),
        for k in range(1,n-i-1):
            print("\b"+str(k)),
        for l in range(n-i-3,0,-1):
            print("\b"+str(l)),
        print(" ")

ndiamond()

