"""
Foundations of Algorithms(CSCI 665)
Author: Shubham Patil
Homework 6, Question 8.b
"""


def knapsack(W, items):
    n = len(items)
    w = [0]
    for i in range(n):
        w.append(items[i][0])

    v = [0]
    for i in range(n):
        v.append(items[i][1])

    DP = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                DP[i][j] = 0
            elif w[i] > j:
                DP[i][j] = DP[i - 1][j]
            else:
                a = v[i] + DP[i - 1][j - w[i]]
                b = DP[i - 1][j]
                DP[i][j] = max(a, b)

    items_selected = []
    j = W
    for i in range(n, 0, -1):
        if DP[i][j] > DP[i - 1][j]:
            items_selected.append(items[i - 1])
            j = j - w[i - 1]
    print("Max possible value:", DP[n][W], "\nWith items, (weight, value) pair:", items_selected)


if __name__ == '__main__':
    W = 11
    # item is (weight, value) pair
    item = [(2, 50), (3, 60), (1, 40), (4, 30), (3, 10)]
    knapsack(W, item)
