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
# use typecasting to break up strings in the middle?

answer = 0

list_init = range(100,1000)
factor_1 = list_init[::-1]
factor_2 = list_init[::-1]

for i,v in enumerate(factor_1):
    f1 = v

    for j,w in enumerate(factor_2):
        f2 = w
        test_ans_num = (f1*f2)
        test_answer = str(f1*f2)

        if (test_ans_num % 2 == 0):
            left = test_answer[0:3]
            right = test_answer[3:]
            right_mir = right[::-1]

            if left == right_mir:
                print(test_ans_num)
                exit("Answer found.")

        elif(test_ans_num % 2 != 0):
            left = test_answer[0:2]
            right = test_answer[3:]

        else:
            pass

exit("Ending script, no solution found.")