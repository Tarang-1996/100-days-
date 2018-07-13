# put all zero in the begining
array = [3,0,5,0,8,4,0,9]
for i in range(0,7):
    if array[i] == 0:
        print(i)
        temp = array[i]
        while(i<7):
           print('temp is',temp)
           array[i] = array[i+1]
           print('array',i,i+1,array[i],array[i+1])
           i=i+1
        array[7] = temp
print(array)
    
    
