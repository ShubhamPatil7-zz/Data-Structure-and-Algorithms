"""
Foundations of Algorithms(CSCI 665)
Author: Shubham Patil
Homework 1, Question 6 :
At n = 31, function fib starts to run slowly noticeably.
"""

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    for i in range(50):
        print("fib(", i, ") = ", fib(i))
