
import math

"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ? """

def first_factors(n):
    l = []
    num = int(math.sqrt(n))
    for i in range(1, num+1):
        if n % i == 0:
            l += [i]
    return l

def other_factors(n):
    ls=[]
    l = first_factors(n)
    for i in l:
        ls += [int(n/i)]
    return ls

def all_factors(n):
    return first_factors(n)+ other_factors(n)

def primes(n):
    p = []
    l = all_factors(n)
    for i in l:
        if len(all_factors(i)) == 2:
            p += [i]
    return max(p)


print(other_factors(600851475143))
print(all_factors(600851475143))
print(primes(600851475143)) #answer is: 6857


"""
Slower way to factor / get primes

def factors(n):
    l = []
    result = []
    for x in range(1, n+1): #gets all the factors of n
        if n % x == 0:
            l +=[x]
    return l

def primes(n):
    p = []
    l = factors(n)
    for k in l:
        f = factors(k)
        if len(f) == 2:
            p += [k]
    return max(p)
"""
