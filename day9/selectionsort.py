#selection sort
num = int(input('enter the number of element '))
array = []
for k in range(0,num):
    array.append([])
for k in range(0,num):
    array[k]=int(input())
for j in range(0,num):
    minimum = array[j]
    l=j+1
    for i in range(l ,num):
        if(minimum>array[i]):
            minimum=array[i]
            p=i
    temp=array[j]
    print(i)
    array[j]=minimum
    array[p]=temp



print(array)
