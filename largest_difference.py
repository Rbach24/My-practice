# write question here
n = int(input("Enter number of elements: "))
a = []
for i in range(0,n):
	x = int(input("Enter number for your first list: "))
	a.append(x)
x = None
y = a[2]
for i in range (0,n):
	if a[i] > x :
		x = a[i]
	if a[i] < y :
		y = a[i]
print(x-y)
