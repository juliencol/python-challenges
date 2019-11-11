def print_list_with_argument(L):
  return L

def print_list_without_argument():
  L = [1, 2, 3]
  return L


def print_element_of_list(L):
  for k in range(len(L)):
    print(L[k])


def sum_list(L):
  sum = 0
  # type some code to calculate the sum of the list
  # hint : use a for loop to go through every element of the list and add it to the sum

  for k in range (len(L)):
    sum = sum + L[k]
  return sum

def sum_of_list(L):
  total = 0
  i = 0
  while i < len(L):
    total += L[i]
    i += 1
  return total

print(sum_of_list([1,2,3]))
