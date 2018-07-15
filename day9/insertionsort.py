#insertion sort
num = int(input('enter the number of element '))
array = []
for k in range(0,num):
    array.append([])
for k in range(0,num):
    array[k]=int(input())
for i in range(1,num):
    j=0
    temp=array[i]
    while(j<=i):
        if(temp<array[j]):
            temp1=array[j]
            array[j]=temp
            temp=temp1
        else:
            array[i]=temp
        j=j+1




print(array)

    

