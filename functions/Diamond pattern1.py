#Write a function diamond() that prints a diamond of height 5.

__*
_***
*****
_***
__*

def diamond():
    #first half of the diamond
    #go through each line
    for i in range(3):
	#print the specified number of spaces in that specific line
        for j in range(2-i):
            print("\b "),
	#print the specified number of stars in that specific line
        for k in range(2*i+1):
            print("\b*"),
	#change the line 
        print(" ")
    #reset the values
    i=0
    j=0
    k=0
    #second half of the diamond
    #repeat the process, but in reverse order
    for i in range(2):
        for j in range(i+1):
            print("\b "),
        for k in range(3-2*i):
            print("\b*"),
        print(" ")

diamond()                                                        
           
