#factorial without recursion
x = input("enter the number? ")
fact = 1
for i in range(1,int(x)+1):
    fact=fact*i
    
print("factorial is",fact)
