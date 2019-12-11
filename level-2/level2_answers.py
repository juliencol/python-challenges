# Exercise 1.1
def get_sum_of_even_elements_in_list_with_for_loop(L):
	result = 0
	for element in L:
		if element % 2 == 0:
			result += element
	return result

# Exercise 1.2
def get_sum_of_even_elements_in_list_with_while_loop(L):
	i = 0
	result = 0
	while(i < len(L)):
		if L[i] % 2 == 0:
			result += L[i]
		i += 1
	return result

# Exercise 2
def are_strings_equals(str1, str2):
	if (len(str1) == len(str2)):
		return False
	for i in range(len(str1)):
		if str1[i] == str2[i]:
			return True
	return False