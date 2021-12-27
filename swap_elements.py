def swapPositions(list, pos1, pos2):

     
	
    list[pos1] , list[pos2] = list[pos2], list[pos1]  

     

    return list
 
# Driver function
#user is smart enough to enter a number
n = int(input("enter number of items in your list "))

list = []
for i in range (0,n):
	list.append(input("enter your input "))



pos1 = int(input("enter first position "))
pos2 = int(input("enter second position "))

if pos1 > len(list) or pos2 > len(list) : 
	print("Invalid input")
	exit()

print(swapPositions(list, pos1-1, pos2-1))
