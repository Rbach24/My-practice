n = int(input("Enter number of items in your list: "))
lis=[]
for i in range(0,n):
	x = input("Enter element")
	lis.append(x)
y = len(lis)
if n%2 == 0: 
	for i in range(0,y/2):
		lis[i], lis[y-i-1] = lis[y-i-1], lis[i]
elif n%2 == 1:
	for i in range (0, y/2 - 1) :
		lis[i], lis[y-i-1] = lis[y-i-1], lis[i]
print(lis)
