n = int(input("Enter the number of items in the list: "))
list = []
for i in range (0,n) :
	x = int(input("Enter number: "))
	list.append(x)
list.remove(max(list))
print(max(list))
