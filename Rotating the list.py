#Given a list and an integer n, write a program to rotate towards left the list by n elements.
#For example: l = [1,2,3,4,5] and n=2 , then the answer should be output=[3,4,5,1,2]


l = [1,2,3,4,5]
n=2

# Your code - begin

i=0
l_new=[]
while i<n:
    l_new.append(l[i])
    i+=1
j=0
while j<len(l_new):
    l.append(l_new[j])
    j+=1

k=0
while k<n:
    l.pop(0)
    k+=1
    
output = l

# Your code - end
print output
