#write a function to iterate a List which is passed in the parameter

n=input()
inp=[]
for i in range(n):
    inp.append(input())
def iterate_list():
    for i in range(len(inp)):
        print(inp[i])
iterate_list()

