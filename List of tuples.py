#You have been given 5 lists. One of the list contains the names of the students, and the other 4 contain their marks in different subjects. Create a list of tuples so that each tuple contains the name of the student and their marks.
#For example: names = [ ’ Malcolm ’ , ’ Timon ’ , ’ Tintin ’ , ’ Bob ’]
#             English = [10 , 15 , 11 , 12]
#             Maths = [9 , 8 ,3 , 1]
#             DS = [10 , 10 , 10 , 10]
#             Physics = [5 , 3 , 1 , 5]

#Then the answer should be:
#[( ’ Malcolm ’ , 10 , 9 , 10 , 5) , ( ’ Timon ’ , 15 , 8 , 10 , 3) , ( ’ Tintin ’ , 11 , 3 ,10 , 1) , ( ’ Bob ’ , 12 , 1 , 10 , 5)]


names = ['Malcolm', 'Timon', 'Tintin', 'Bob']
English = [10, 15, 11, 12]
Maths = [9, 8,3, 1]
DS = [10, 10, 10, 10]
Physics = [5, 3, 1, 5]

# Your code - begin

length=len(names)
information=[]
i=0
while i<length:
    information.append((names[i],English[i],Maths[i],DS[i],Physics[i]))
    i+=1
output = information

# Your code - end
print output
