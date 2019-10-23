#Given a function isPalindrome(n) that checks whether a given number (or string) is a palin- drome or not. isPalindrome makes use of another function recurse(n, i) which implements actual check using recursion. Implement recurse .

def recurse(n, i):
## Your code - begin

    #check if length of n at particular movement is equal to i(for numbers having even length) or i+1(for numbers having odd length)
    if len(n)==i or len(n)==i+1:
        return True
    #increase i by one through each recursive call and compare this index element with last element
    #also remove last element through each recursive call
    elif n[i]!=n[len(n)-1]:
        return False
    #call the function recursively
    return recurse(n[:len(n)-1],i+1)

## Your code - end

def isPalindrome(n):
  return recurse(n, 0)
  

