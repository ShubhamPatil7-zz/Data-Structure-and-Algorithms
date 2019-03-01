"""
Foundations of Algorithms(CSCI 665)
Author: Shubham Patil
Homework 1, Question 8 :
function fibIt does not run slowly at n = 31, in fact it runs quickly even for n = 900.
"""

def fibItHelper(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibItHelper(n-1, b, a+b)


def fibIt(n):
    return fibItHelper(n, 0, 1)


if __name__ == '__main__':
    for i in range(901):
        print("fibIt(", i, ") = ", fibIt(i))