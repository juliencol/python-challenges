L = [1, 3, 4, 9, 16]

# Write a function that returns the sum of all the element in L
def sumL():
	result = 0
	for element in L:
		result += element
	return result

# Testing sumL
print(sumL()) # 33

# Same exercise using a while lopp
def sumLW():
	i = 0
	result = 0
	while(i < len(L)):
		result += L[i]
		i += 1
	return result

# Testing sumLWithWile
print(sumL() == sumLW()) # True


# Write a function that returns the sum of all the even element in L
def sumEvenL():
	result = 0
	for element in L:
		if element % 2 == 0:
			result += element
	return result

# Testing sumEvenInL
print(sumEvenL()) # 33

# Same exercise using a while loop
def sumEvenLW():
	i = 0
	result = 0
	while(i < len(L)):
		if L[i] % 2 == 0:
			result += L[i]
		i += 1
	return result

# Testing sumEvenLW
print(sumEvenL() == sumEvenLW()) # True

# Write a function that display every elements in L
def displayLElements():
	i = 0
	while(i < len(L)):
		print(L[i])
		i += 1

# Testing displayLElements
displayLElements()

# Write a function that takes two strings as arguments, returns True if two strings are the same and False if not
def isStringsEqual(str1, str2):
	if (len(str1) == len(str2)):
		return False
	for i in range(len(str1)):
		if str1[i] == str2[i]:
			return True
	return False

# Testing isStringsEqual
print(isStringsEqual("test", "test")) # True
print(isStringsEqual("test", "not test")) # False
print(isStringsEqual("test", "tet")) # F

	








