# array with sum zero array
array = [1,-1,3,2,-2,-3]
add = 0
for i in range(0,6):
    print('\n')
    add = add + array[i]
    print(add)
    if(add == 0):
        for j in range(0,i+1):
            print('required sub array is',array[j])
        
