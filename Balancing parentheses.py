#Write a program to check if a given expression has balanced parentheses.The input string is allowed to contain only three types of brackets: parentheses, i.e. ’(’ / ’)’ , curly braces ’{’ / ’}’ and square brackets ’[’ / ’]’.
#refer: https://www.youtube.com/watch?v=QZOLb0xHB_Q

inp = "([[]])[{}]"
# Your code - begin
opening=['(','[','{']
closing=[')',']','}']
i=0
s=[]
while i<len(inp):
    if inp[i] in opening:
        s.append(inp[i])
    elif inp[i] in closing:
        if len(s)==0:
            output='NOT BALANCED'
        else:
            if inp[i]==')' and s[len(s)-1]=='(':
                s.pop()
            elif inp[i]==']' and s[len(s)-1]=='[':
                s.pop()
            elif inp[i]=='}' and s[len(s)-1]=='{':
                s.pop()
            else:
                output='NOT BALANCED'
    else:
        output='INVALID INPUT'
    i+=1
if len(s)==0:
    output='BALANCED'
else:
    output='NOT BALANCED'

# Your code - end
print output
