n = int(input("Enter number of elements: "))
list = []
for i in range (0,n):
	x = input("Enter your number : ")
	list.append(x)
y = 0 
new_list = []
for j in list:
	for k in str(j) : 
		y = y + int(k)
	new_list.append(y)
	y = 0

print(new_list)
