#Write a function ndiamond() that prints a numerical diamond of height 5.

#__1
#_121
#12321
#_121
#__1

def ndiamond():
    #first half of the pattern
    #go to each line
    for i in range(3):
	#print specific number of spaces (depending upon the value of i)
        for j in range(2-i):
            print("\b "),
	#print the specific accending numbers in same line
        for k in range(1,i+2):
            print("\b"+str(k)),
	#print the specific descending numbers in same line
        for l in range(i,0, -1):
            print("\b"+str(l)),
	#go to next line
        print(" ")
    #reset the values
    i=0
    j=0
    k=0
    l=0
    #second half of the pattern 
    #simillarly print in reverse order
    for i in range(2):
        for j in range(i+1):
            print("\b "),
        for k in range(1,3-i):
            print("\b"+str(k)),
        for l in range(1-i,0,-1):
            print("\b"+str(l)),
        print(" ")

ndiamond()

