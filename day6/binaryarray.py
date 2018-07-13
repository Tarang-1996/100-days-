# put all zero in the begining
array = [1,0,1,0,1,0,1,0,0,0,1]
for i in range(0,10):
    if array[i] == 0:
        print(i)
        temp = array[i]
        while(i>0):
           print('temp is',temp)
           array[i] = array[i-1]
           print('array',i,i-1,array[i],array[i-1])
           i=i-1
        array[0] = temp
print(array)
    
    
