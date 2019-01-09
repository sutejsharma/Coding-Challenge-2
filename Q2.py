s1 = input("Please input string1: ")
s2 = input("Please input string2: ")

try:	
	#This check is for numeric values ; to see which is greater between the two. For example: -1 vs 0.36, 10 vs -2 and so on
	if type(float(s1)) and type(float(s2)):
		if(float(s1) < float(s2)):
			print("string1 number is smaller than string2 number")
		elif(float(s1) == float(s2)):
			print("string1 number is equal to string2 number")
		else:
			print("string1 number is larger than string2 number")

except ValueError:
	#If the string is non-numeric, then the length of the strings are compared as well as their ordinal values.
	if(len(s1) == len(s2)):
		if(s1 == s2):
			print("The strings are exactly equal in length and ordinal value")
		elif(s1>s2):
			print("The strings are exactly equal in length, but string1 has higher ordinal value than string 2")
		else:
			print("The strings are exactly equal in length, but string2 has higher ordinal value than string 1")

	elif(len(s1) > len(s2)):
		if(s1 == s2):
			print("string1 is longer than string 2, but both have same ordinal value")
		elif(s1>s2):
			print("string1 is longer than string 2, but string1 has higher ordinal value than string 2")
		else:
			print("string1 is longer than string 2, but string2 has higher ordinal value than string 1")

	else:
		if(s1 == s2):
			print("string2 is longer than string 1, but both have same ordinal value")
		elif(s1>s2):
			print("string2 is longer than string 1, but string1 has higher ordinal value than string 2")
		else:
			print("string2 is longer than string 1, but string2 has higher ordinal value than string 1")