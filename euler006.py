import numpy as np

a = list(range(1,101))

def f():
    sum_of_squares = 0
    for i in range(len(a)):
        sum_of_squares += a[i]**2

    square_of_sum = sum(a)**2

    return square_of_sum-sum_of_squares

print(f())
