# Exercises on variables, lists, for and while loops and functions

def print_list_with_argument(L):
    """ This function prints a list given as an arugment. """
    return L

def print_list_without_argument():
  """ This function prints the list containing 1, 2, 3 and doesnt have any parameter."""
  L = [1, 2, 3]
  return L

def print_element_of_list(L):
  """ Given a list in arguement, this function prints every element of that list. """
  for k in range(len(L)):
    print(L[k])
    
def sum_list_for(L):
  """ Given  a list in argument, this function calculates the sum of every element in the list,
  using a for loop. """ 
  sum = 0
  for k in range (len(L)):
    sum = sum + L[k]
  return sum

def sum_of_list_while(L):
  """ Given  a list in argument, this function calculates the sum of every element in the list,
  using a while loop. """ 
  total = 0
  i = 0
  while i < len(L):
    total += L[i]
    i += 1
  return total

def repetitions(x, k):
    """ Given an element and an integer k as arguments,
    this function returns a list containing k times the element. """ 
    L = []
    for i in range(k):
        L.append(x)
    return L

def repetition_block(L, k):
    """ Given a list and an integer k as arguments, this function returns a list containing
    k times the list given. """
    new_L = []
    for i in range(k):
        for j in range(len(L)):
            new_L.append(L[j])
    return new_L

def max_list(L):
    """ Given a list as an arguement, this function return the maximum element in the list. """ 
    max = L[0]
    for i in range(len(L)):
        if L[i] > max:
            max = L[i]
    return max

def nb_occurences(L, element):
    """ Given a list and an element as arugments; this function returns
    the number of times the element appears in that list. """ 
    occ = 0
    for k in range(len(L)):
        if L[k] == element:
            occ += 1
    return occ
    