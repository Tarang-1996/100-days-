def is_leap(year):
    leap = False
    if year % 4 == 0 or year % 400 == 0:
        return True
    else:
       return leap
year = int(input())
print(is_leap(year))




for i in range(1, 11):
    print(i, end='')


n = int(input())
if N % 4 == 0 or N >20 and N % 2 == 0:
    print("Not Weird")
elif N % 2 == 0 and N >=6 and N <= 20:
    print('Weird')
else:
    print('Weird')

