#Given a function decToBin(n) that returns the binary equivalent of the number n. decToBin makes use of another function recurse(ans, n) which implements the decimal to binary conversion using recursion. Implement recurse .

def recurse(ans, n):
## Your code - begin

    #first write the base condition
    #i.e if the number n becomes zero, return string
    if n==0:
        return ans
    #else return n/2 after storing n%2 in string(ans)
    return recurse(str(n%2)+ans, n/2)

## Your code - end

def decToBin(n):
  return recurse("", n) 


