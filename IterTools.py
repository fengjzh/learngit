#!/bin/python36
def Pi(N):
    sum = 0.0
    f = 4
    for item in itertools.takewhile(lambda x:x<=2*N-1,itertools.count(1,2)):
        sum = sum + f/item
        f = -f
    return sum
print(Pi(10))
print(Pi(100))
print(Pi(1000))
print(Pi(10000))
