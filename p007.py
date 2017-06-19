#!/usr/bin/python

# Ravi Bhikhie
# Euler Project
# https://projecteuler.net/problem=7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
from __future__ import print_function

# I probably need to to implement a prime finding algorithm here.
# NOTE: need to watch out for off-by-one errors.

# starting count at 7, because the first six primes are given.
prime = 7

while True:
    prime = prime + 1 
    break

print("Exited while loop.")
print("Prime found: ", prime)

exit()

