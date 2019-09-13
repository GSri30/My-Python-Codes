#Write a function diamond(n, c) that prints a diamond of height n made of character c,
#where n is an odd number. Your function is not expected to behave deterministically if n
#is not an odd number. For example, diamond(3, ’1’) will give:

#_1
#111
#_1

def diamond(n, c):
    #run the nested loops only when the input is odd number
    if n%2!=0:
	#first half of the pattern
	#go to each line
        for i in range((n+1)/2):
	    #print the specific number of spaces for that particular line (particular i value)
            for j in range(((n+1)/2)-i-1):
                print("\b "),
	    #print the specific number of input message for that particular line (particular i value)
            for k in range(2*i+1):
                print("\b" + c),
	    #leave the current line
            print(" ")
	#reset the values
        i=0
        j=0
        k=0
	#second half of the pattern
	#perform the same in reverse order (decreasing order)
        for i in range((n-1)/2):
            for j in range(i+1):
                print("\b "),
            for k in range(n-2*i-2):
                print("\b" + c),
            print(" ")

diamond()


