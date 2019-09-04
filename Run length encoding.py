from Q1input import *

# Your code - begin
i=0
output1=[]
output2=[]
output=''
count=1
while i<len(inp):
    if not inp[i] in output1:
        output1.append(inp[i])
        output2.append(1)
    else:
        j=output1.index(inp[i])
        output2[j]+=1
    i+=1
j=0
while j<len(output1):
    output+=str(output2[j])+output1[j]
    j+=1
 

# Your answer should be placed in this variable.
# Your code - end

print (output)
