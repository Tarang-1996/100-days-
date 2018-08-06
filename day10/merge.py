num = int(input('enter the number of element '))
array = []
for k in range(0,num):
    array.append([])
for k in range(0,num):
    array[k]=int(input())
i=0
j=num
def divide(i,j):
    while i<j:
         mid = (i+j)/2
         print('mid')
         divide(i,mid)
         print(mid)
         divide(mid+1,j)
         print(mid)


print(array)
