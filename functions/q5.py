#Write a function which takes 2 lists of same length and adds respective elements using another function.List can either have number or string

n=input()
list1=[]
list2=[]
for i in range(n):
    list1.append(input())
for j in range(n):
    list2.append(input())

def add_respective_elements():
    for k in range(n):
        print(list1[k]+list2[k])

add_respective_elements()
