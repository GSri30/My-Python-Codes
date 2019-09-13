#Write a function diamond(n) that prints a diamond of height n, where n is an odd number.
#Your function is not expected to behave deterministically if n is not an odd number. For
#example, diamond(3) will give:

#_*
#***
#_*

def diamond(n):
    #perform only if the input (n) is odd 
    if n%2!=0:  
	#first half of the diamond
	#go to each line        
	for i in range((n+1)/2):
	    #print the specific number of spaces in the same line
            for j in range(((n+1)/2)-i-1):
                print("\b "),
	    #print the specific number of stars in the same line
            for k in range(2*i+1):
                print("\b*"),
	    #change the line
            print(" ")
	#reset the values
        i=0
        j=0
        k=0
	#second half of the diamond
	#perform the same in reverse order
        for i in range((n-1)/2):
            for j in range(i+1):
                print("\b "),
            for k in range(n-2*i-2):
                print("\b*"),
            print(" ")

diamond()

