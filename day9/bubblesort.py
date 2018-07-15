num = int(input('enter the number of element '))
array = []
for k in range(0,num):
    array.append([])
for k in range(0,num):
    array[k]=int(input())
j=num-1
while j>=0:
    for i in range (0,j):
        if array[i]>array[i+1]:
            temp = array[i]
            array[i]=array[i+1]
            array[i+1]=temp
    j=j-1
        
    
print(array)    
