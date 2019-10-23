#Implement a function even_elements(l) that takes an input list l and returns a list only even elements from l . Use list comprehension to achieve this

def even_elements(l):
## Your code - begin

    #return a list by adding the elements of given list if the element is divisible by 2
    return [x for x in l if x%2==0]

## Your code - end
  

