import math

# Exercise 1
def get_circle_area(R):
    return math.pi * R ** 2

# Exercise 2.1
def reverse_names(firstName, lastName):
    firstName, lastName = list(firstName), list(lastName)
    firstName.reverse(), lastName.reverse()
    newFirstName, newLastName = "".join(firstName), "".join(lastName)
    return newFirstName + " " + newLastName

# Exercise 2.2
def my_reverse_names(firstName, lastName):
    firstName, lastName = list(firstName), list(lastName)
    newFirstName, newLastName = '', ''
    for i in firstName:
        newFirstName = i + newFirstName
    for i in lastName:
        newLastName = i + newLastName
    return newFirstName + " " + newLastName
