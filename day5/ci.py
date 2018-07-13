# generate problem of sum
money = input('enter the amonut to calculate compound interest ')
rate = input('enter the rate ')
time = input('enter the time ')
p = int(money)
r = float(rate)
t = float(time)
R = r / 100
T = pow(R,t)
ci = (p * (1 + T)) - p
print('compound interest is',R,T,ci)
