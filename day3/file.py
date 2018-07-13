items = input('number of items you want to enter?  ')
file = open("grocery.txt","w")
file.write("LIST of grocery is following")
file.close()
x = int(items)
i=1
while i<=x:
      file = open('grocery.txt','a')
      name = input('enter the name of item ')
      quantity = input('enter the quantity of item ')
      file.write("\n"+ str(i)+ "  " + name + "  " + "=>" + "  " + quantity)
      file.close()
      i=i+1
file = open("grocery.txt","r")
f1 = file.readlines()
for lines in f1:
    print(lines[pulse])
       

