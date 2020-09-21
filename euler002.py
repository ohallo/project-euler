


"""Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""
def fibmaker(n):
    list= [1,2]
    i = 2
    v = list[i-2]+list[i-1]
    while v < n:
        list+=[v]
        i+=1
        v = list[i-2]+list[i-1]
    return list


def f(l):
    total = 0
    for x in l:
        if x % 2 == 0:
            total+=x
    return total



print(f([1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 44)
print(fibmaker(4000001))
print(f(fibmaker(4000001)))
