# Ravi Bhikhie
# Euler Project

# Problem 004
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Upper bound for numbers = 999
# Lower bound for numbers = 100
# max_product = 998001
# min_product = 10000
#
# This is to approach from the other way: Create a list of all possible solutions and evaluate it backwards.

populate = range(999, 99, -1)
solutions = []

# Create list with all possible 6-digit solutions
for el in populate:
    left = str(el)
    right = left[::-1]
    test = int(left+right)
    solutions.append(test)

# Start actual evaluation
for ans in solutions:
    for fac in populate:
        if ans == 999999:
            continue
        if ((ans % fac == 0) and (len(str(ans/fac))) <=3 ):
            print fac
            print ans
            exit("Solution found!")

exit("Nothing found :( Something went wrong!")
