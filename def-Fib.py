#!/bin/python36
def Fib(max):
    n,a,b=0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n=n+1
for n in Fib(10):
    print(n)
