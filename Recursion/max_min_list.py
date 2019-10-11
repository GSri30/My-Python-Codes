#Write a function to find minimum and maximum element in a list using recursion

def maximum(listt,n):
    if n==1:
        return listt[0]
    return max(listt[n-1],maximum(listt,n-1))

def minimum(listt,n):
    if n==1:
	return listt[0]
    return min(listt[n-1],minimum(listt,n-1))
