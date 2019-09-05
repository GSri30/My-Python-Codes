#Program to find the median of a given unsorted list


l = [13, 18, 13, 14, 13, 16, 14, 21, 13]
# Your code - begin

#sorting the elements
i=0
while i<len(l):
    j=i+1
    while j<len(l):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
        j+=1
    i+=1

#computing median
n=len(l)
if n%2==0:
    median=(l[n/2-1]+l[n/2])/2.0
else:
    median=l[(n-1)/2]

output = median 

# Your code - end
print output
