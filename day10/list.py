#list manipulation
x = [5,1,9,2,7,3,4,6,45,2,6,9,8,4,3,6]
print(x)
print('''******************append******************************
*****************************LIST******************************''')
x.append(12)
print(x)
print('*********************insert in list***************************')
x.insert(9,1258)
print(x)
print('*********************remove in list***************************')
x.remove(2)
print(x)
print('*********************index of any number  in list***************************')
print(x.index(45))
print('*********************count occurance of any number  in list***************************')
print(x.count(6))
print('*********************sort the list***************************')
x.sort()
print(x)

