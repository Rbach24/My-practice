n = int(input("Enter number of items : "))
a = []
b = []
for i in range (0,n):
	#adding items
	x = int(input("Enter number for your first list: "))
	a.append(x)
	
for i in range (0,n):
	#adding items
	y = int(input("Enter number for your second list: "))
	b.append(y)
print(a)
print(b)
c = []
for i in range (0, n) :
	c.append(a[i]+b[i])

print(c)	
		
