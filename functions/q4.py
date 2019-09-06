#pass two lists as parameter and print the common elements

n1=input()
n2=input()
list1=[]
list2=[]
result=[]
for i in range(n1):
    list1.append(input())
for i in range(n2):
    list2.append(input())

def common_elements():
    for ele in list1:
        if ele in list2:
            result.append(ele)
    print(result)

common_elements()
