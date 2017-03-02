# Ravi Bhikhie
# Euler Project
#
# Problem 003
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

target = 600851475143 #600851475143
factors = []
f = 2

while target > 1:
    if target % f == 0:
        factors.append(f)
        target = target / f
        if f <= 1:
            break
        f = 2
    else:
        f = f + 1

print factors