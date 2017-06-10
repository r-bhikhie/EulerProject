# Ravi Bhikhie
# Euler Project

# Problem 004
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

# Upper bound for numbers = 999
# Lower bound for numbers = 100
# max_product = 998001
# min_product = 10000
#
# use typecasting to break up strings in the middle?

answer = 0

list_init = range(100,1000)
factor_1 = list_init[::-1]
factor_2 = list_init[::-1]

print factor_2[1]

for a,b in enumerate(factor_1):
    #print(b,a)
    pass

exit("Ending script.")