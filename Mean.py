#Program to find the mean of a given unsorted list


l = [13, 18, 13, 14, 13, 16, 14, 21, 13]

# Your code - begin
count=0
k=0
while k<len(l):
    count+=l[k]
    k+=1
mean=float(count)/float(len(l))

output = mean

# Your code - end
print output
