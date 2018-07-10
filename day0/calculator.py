z=1
x = input('enter the first digit? ')
y = input('enter the second digit? ')
expr = input('enter the operation? ')

    
if expr == '*' :
    print(int(x)*int(y))

elif expr == '+' :
    print(int(x)+int(y))

elif expr == '-' :
    print(int(x)-int(y))   

elif expr == '/' :
    print(int(x)/int(y))   

elif expr == '%' :
    print(int(x)%int(y))

else:
    print('enter the valid operation')
    
