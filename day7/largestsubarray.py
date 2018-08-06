#largest subarray of consecutive intergers
array = [10,5,2,9,3,0,7,6,4]
subarray = []
i=0
array.sort()
print(array)
for i in range(0,9):
    for j in range(0,9):
        if i == array[j]:
            print(i)
        
