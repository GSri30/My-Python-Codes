#You are given a function printSeq(n, k) that takes 2 integers as inputs: n and k. The goal is to print all sequences of k-length, where the elements of the sequences are from first n natural numbers, and the digits in the k sequence are increasing, that is digit at k th is greater than the digit at (k − 1) th position. printSeq makes use of another function printSeqUtil(n, k, len1, arr) which does the actual work of printing the sequences; printSeqUtil is recursive.

# Array printing utility function. Feel free to use.
def printArr(arr, k): 
    for element in range(k):
        print(arr[element]),
    print(" ")
  
def printSeqUtil(n, k, len1, arr):  
## Your code - begin

    #if the length of the array is equal to required sub sequences length,print the elements of the array in the same line
    if len1==k:
        printArr(arr,k)
        return
    #if no elements are present in the array, then create a variable and assign one to it
    if len1==0:
        current_position=1
    #else give the variable a value which is equal to the one more than the last value 
    else:
        current_position=arr[len1-1]+1
    
    #increase the length of the array (variable which stores the length of the array)
    len1+=1

    #start a loop to store the elements (subsequences) starting with a specific number(greater than that specific number and also each number is greater than previously stored number)
    while current_position<=n:
        arr[len1-1]=current_position
        #call the function recursively to store the numbers greater than the previous number stored
        printSeqUtil(n,k,len1,arr)
        current_position+=1
    #reset the value of length of array so that it can be used for the next loop call 
    len1-=1

## Your code - end
  
def printSeq(n, k): 
    arr = [0] * k  
    len1 = 0
    printSeqUtil(n, k, len1, arr) 

