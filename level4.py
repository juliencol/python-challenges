# Warning
# All following functions can takes up to 3 arguments as input but should only return one value as output



# Exercise 1 (easy)
# Implement the following function get_triangle_area
# input: base of a triangle, height of a triangle (both in centimeters)
# output: area of the triangle

def get_triangle_area(base, height):
    return 0

# Test your code for exercise 1
print(get_triangle_area(2, 3))  # 3
print(get_triangle_area(4, 2))  # 4



# Exercise 2 (easy)
# A number is symmetrical when it is the same as its reverse. ()
# Implement the following function is_symmetrical
# output: True or False depending if the input is a symmetrical number or not

def is_symmetrical(number):
    return 0

# Test your code for exercise 2
print(is_symmetrical(7227))  # True
print(is_symmetrical(12567))  # False



# Exercise 3 (medium)
# Implement the following function get_multiples
# input: number (integer), length(integer)
# output: list of multiples of number up to length

def get_multiples(number, length):
    return 0

# Test your code for exercise 3
print(get_multiples(7, 5))  # [7, 14, 21, 28, 35]
print(get_multiples(12, 10))  # [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]



# Exercise 4 (medium)
# A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct solutions for x.
# Implement the following function get_quadratic_equation_solution
# input: a, b and c coefficients of a quadratic equation
# output: number of solutions and solutions formatted in a string

def get_quadratic_equation_solutions(a, b, c):
    return 0

# Test your code for exercise 4
print(get_quadratic_equation_solutions(1, 0, -1)) # the given equation has two solutions: x = 1 and x = -1
print(get_quadratic_equation_solutions(1, 0, 0)) # the given equation has one solution: x = 0
print(get_quadratic_equation_solutions(1, 0, 1)) # the given equation has no solutions



# Exercise 5 (hard)
# Implement the following function insert_white_space
# input: phrase without white spaces ("SheWalksToTheBeach")
# output: phrase with white spaces ("She Walks To The Beach")

def insert_white_space(phrase):
    return 0

# Test your code for exercise 5
print(insert_white_space("SheWalksToTheBeach")) # "She Walks To The Beach"
print(insert_white_space("MarvinTalksTooMuch")) # "Marvin Talks Too Much"



# Exercise 6 (hard)
# A positive number greater than 1 can be defined untouchable when it's not equal to the sum of the proper divisors
# of any other positive number, in a range starting from 2 and ending with the square of the given number (bounds included).
# Implement the following function is_untouchable
# input: a given number (integer)
# output: a boolean set to True if the given number is untouchable and False if not

def is_untouchable(number):
    return 0

# Test your code for exercise 6
print(is_untouchable(2)) # True
print(is_untouchable(3)) # False

# Bonus question for exercise 6
# Find a way to modify your code so it can handles error and display a warning message if the given number is lower than 2
