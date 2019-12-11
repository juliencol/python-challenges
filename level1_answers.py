# Exercise 1
def get_list(L):
    return L

# Exercise 2.1
def get_sum_of_elements_in_list_with_for_loop(L):
    sum = 0
    for k in range(len(L)):
        sum = sum + L[k]
    return sum

# Exercise 2.2
def get_sum_of_elements_in_list_with_while_loop(L):
    sum = 0
    i = 0
    while i < len(L):
        sum += L[i]
        i += 1
    return sum

# Exercise 3.1
def repetitions(x, k):
    L = []
    for i in range(k):
        L.append(x)
    return L

# Exercise 3.2
def repetition_block(L, k):
    new_L = []
    for i in range(k):
        for j in range(len(L)):
            new_L.append(L[j])
    return new_L

# Exercise 4
def number_of_occurrences(L, element):
    occ = 0
    for k in range(len(L)):
        if L[k] == element:
            occ += 1
    return occ

# Exercise 5
def max__element_in_list(L):
    max = L[0]
    for i in range(len(L)):
        if L[i] > max:
            max = L[i]
    return max
