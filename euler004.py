"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindrome(n): #n is number as a string
    result = True
    for i in range(len(n)):
        if n[i] != n[len(n)-1-i]:
            result = False
    return result

def palindrome(n):
    threedigit = 1
    for i in range(100, 1000):
        intgr = int(n)
        num = intgr*i
        if is_palindrome(str(num)):
            threedigit = i
    return intgr*threedigit

def answer():
    l = []
    for i in range(100,1000):
        l += [largest_palindrome(i)]
    return max(l)


print(is_palindrome("90000009"))
print(is_palindrome("9889"))
print(is_palindrome("9019"))
print(palindrome("909"))
print(answer())
