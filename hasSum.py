"""
Foundations of Algorithms(CSCI 665)
Author: Shubham Patil
Homework 3, Question 4.a & 4.b
"""
from q5 import QuickSort


def HasSum(S, x):
    QuickSort(S)
    return SortedHasSum(S, x)


def SortedHasSum(S, x):
    left = 0
    right = len(S) - 1
    while left < right:
        sum = S[left] + S[right]
        if sum == x:
            return True
        else:
            if sum < x:
                left += 1
            if sum > x:
                right -= 1
    return False


if __name__ == '__main__':
    S = [10, 12, 25, 34, 74]
    x = 22
    print(SortedHasSum(S, x))
    S2 = [25, 34, 10, 74, 12]
    print(HasSum(S2, x))
