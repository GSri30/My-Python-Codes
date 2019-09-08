#Given a sorted list, and another unsorted list, write a program to insert the elements of the second list into the first list such that the sorted nature of the first list is maintained.
#For example: l1 = [ 2, 5, 8, 10, 15] and l2 = [3, 4, 1, 9, 7] then ans = [1, 2, 3, 4, 5, 7, 8, 9, 10, 15] .
#Note: The two lists could be of different lengths. And there won't be any integer which appears in the both the lists.


l1 = [ 2, 5, 8, 10, 15]
l2 = [3, 4, 1, 9, 7]

# Your code - begin
i=0
while i<len(l2):
    l1.append(l2[i])
    i+=1
j=0
while j<len(l1):
    k=j+1
    while k<len(l1):
        if l1[j]>l1[k]:
            l1[j],l1[k]=l1[k],l1[j]
        k+=1
    j+=1


output = l1

# Your code - end
print output
