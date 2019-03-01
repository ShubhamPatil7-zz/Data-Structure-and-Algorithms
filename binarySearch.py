"""
Foundations of Algorithms(CSCI 665)
Author: Shubham Patil
Homework 3, Question 3
"""
from math import ceil


def search(a, v):
    l = 0
    h = len(a) - 1
    while l <= h:
        m = l + ceil((h - l)/2)
        if a[m] == v:
            return True
        if a[m] > v:
            h = m - 1
        if a[m] < v:
            l = m + 1
    return False


if __name__ == '__main__':
    a = list(range(10))
    for i in range(11):
        print(i, search(a, i))

