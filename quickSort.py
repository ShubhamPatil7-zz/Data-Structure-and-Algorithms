"""
Foundations of Algorithms(CSCI 665)
Author: Shubham Patil
Homework 3, Question 5
"""

def QuickSort(a):
    QuickSortHelper(a, 0, len(a) - 1)


def QuickSortHelper(a, p, r):
    while p < r:
        q = partition(a, p, r)
        if r - q < q - p:
            QuickSortHelper(a, q + 1, r)
            r = q - 1
        else:
            QuickSortHelper(a, p, q - 1)
            p = q + 1


def partition(a, p, r):
    x = a[p]
    i = p + 1
    j = r
    while i <= j:
        if a[i] <= x:
            i = i + 1
        elif x < a[j]:
            j = j - 1
        else:
            a[i], a[j] = a[j], a[i]
    a[p], a[i - 1] = a[i - 1], a[p]
    return i - 1


if __name__ == '__main__':
    l = [54, 33, 21, 12, 87, 95, 32, 87, 35, 98, 12]
    QuickSort(l)
    print(l)
