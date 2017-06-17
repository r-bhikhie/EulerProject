# Ravi Bhikhie
# Euler Project
#
# Problem 006
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

from __future__ import print_function

sum_of_squares = 0

# rewriting the sum of 1 to 100:
sqare_of_sum = (50*101)**2

working_set = range(1, 101)

for i in working_set:
    addnum = i*i
    sum_of_squares = sum_of_squares + addnum

print(sqare_of_sum - sum_of_squares)

exit()
# blip
