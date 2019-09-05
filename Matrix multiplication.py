#Program to calculate the product of two matrices.(only if they are multiplicable)

m1 = [[0, -1, 2], [4, 11, 2]]
m2 = [[3, -1], [1, 2], [6, 1]]

# Your code - begin
lenm1m=len(m1)
lenm2m=len(m2)
lenm1n=len(m1[0])
lenm2n=len(m2[0])
a=0
b=0
#making an empty matrix
result = []
for a in range (0,lenm1m):
    result.append([])
for a in range (0,lenm1m):
    for b in range (0,lenm2n):
        result[a].append(b)
        result[a][b] = 0
#computing multiplication
if lenm1n==lenm2m:    
    for i in range (0,lenm1m):
        for j in range(0,lenm2n):
            for k in range(0,lenm2m):
                (result[i][j])+=(m1[i][k]*m2[k][j])

    output=result
    
else:
    output='NOT MULTIPLICABLE'



# Your code - end
print output
