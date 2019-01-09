x1 = int(input("Input x1 value for line 1: "))
x2 = int(input("Input x2 value for line 1: "))
x3 = int(input("Input x3 value for line 2: "))
x4 = int(input("Input x4 value for line 2: "))

print(x1, type(x1))
print(x2, type(x2))
print(x3, type(x3))
print(x4, type(x4))

""" 
x1 is the first point in line 1 and x2 is the second point in line 1
x3 is the first point in line 2 and x4 is the second point in line 2
The logic takes into account for positive values and negative values for x1,...,x4 and computes if an overlap exists between the lines.
The absolute function is used to take into account negative values
"""
if(x1<=x3 and x3<abs(x2)) or (x3<=x1 and x1<abs(x4)):  
	print("Overlap exists")
elif(x1==x2==x3==x4):
	print("All the coordinates are at the same point")
else:
	print("No overlap")