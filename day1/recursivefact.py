x = input("value is? ")
z = int(x)
fact = 1
def factorial(num):
    if num <=1 :
        return 1
    else:
        a = factorial(num-1)
        num = num * a
        return num

y = factorial(z)
print("factorial is ",y)
