
num1 = input('enter the num1 ')
num2 = input('enter the num2 ')
x = int(num1)
y = int(num2)
i = x
while 1:
      if  i % y == 0:
             lcm = i
             break
      else:
            i = x + i
            lcm = i
    

print ('lcm is',i)

while x != y:
        if x > y:
          x = x-y
        else:
          y = y-x
print('hcf is',x)
