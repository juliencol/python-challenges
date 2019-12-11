import math

# Exercise 1
# Write a function that returns the area of a circle given its radius R as a parameter


def getArea(R):
    return math.pi * R ** 2

# Testing getArea
# print(getArea(2)) # 6.28

# Exercise 2
# Write a Python program which accepts the user's first and last name and print
# them in reverse order with a space between them.


def reverseName(firstName, lastName):
    firstName, lastName = list(firstName), list(lastName)
    firstName.reverse(), lastName.reverse()
    newFirstName, newLastName = "".join(firstName), "".join(lastName)
    return newFirstName + " " + newLastName

# Testing reverseName
# print(reverseName("julien", "colombain"))
# print(reverseName("alexandre", "jallet"))


def myReverseName(firstName, lastName):
    firstName, lastName = list(firstName), list(lastName)
    newFirstName, newLastName = '', ''
    for i in firstName:
        newFirstName = i + newFirstName
    for i in lastName:
        newLastName = i + newLastName
    return newFirstName + " " + newLastName


# Testing myReverseName()
print(myReverseName("julien", "colombain"))
print(myReverseName("alexandre", "jallet"))


# Exercise 4
# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
