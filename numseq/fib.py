'''This file returns fibonacci's number'''

def fib(num):
    result = 0
    second = 1
    for first in range(2,num):
        result = first + second
        second = first
    return result