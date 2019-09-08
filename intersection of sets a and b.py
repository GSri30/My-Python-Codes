l1=['s','d','h']
l2=['t','s','h']
l3=[]
i=0
while i<len(l1):
    if l1[i] in l2:
        l3.append(l1[i])
        i+=1
    else:
        i+=1

print(l3)
