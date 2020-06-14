import numpy
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
l = numpy.arange(1000)



def f(l):
    total = 0
    for x in l:
        if x % 3 == 0:
            total += x
        elif x % 5 == 0:
            total += x
        else:
            total += 0

    return total
    print(total)

print(f([1,2,3,4,5,6,7,8,9]) == 23)
print(f(l))
