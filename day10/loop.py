x = int(input('enter the no of rows in matrix '))
y = int(input('enter the no of columns in matrix '))
mat = []
for i in range(0,x):
    mat.append([])
for i in range(0,x):
    for j in range(0,y):
        mat[i].append(j)
        mat[i][j]=0
for i in range(0,x):
    for j in range(0,y):
        print('\n')
        mat[i][j]='*'
        print(mat)
        

