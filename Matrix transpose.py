#Program to find transpose of a matrix

m1 = [[0, -1, 2], [4, 11, 2]]

# Your code - begin
lenm1m=len(m1)
lenm1n=len(m1[0])
transpose=[]
#making an empty matrix
for a in range (0,lenm1n):
    transpose.append([])
for a in range (0,lenm1n):
    for b in range (0,lenm1m):
        transpose[a].append(b)
        transpose[a][b] = 0
#computing transpose
for i in range (0,lenm1m):
    for j in range(0,lenm1n):
        transpose[j][i]=m1[i][j]
output=transpose

# Your code - end
print output
