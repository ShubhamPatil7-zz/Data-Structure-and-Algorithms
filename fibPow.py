"""
Foundations of Algorithms(CSCI 665)
Author: Shubham Patil
Homework 2, Question 3
Time complexity of fibPow(n) is O(lg(n)).
"""


class Fibonacci:
    __slots__ = "matrix"

    def __init__(self):
        self.matrix = [[1, 1], [1, 0]]

    def fibPow(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.L(self.matrix, n-1)[0][0]

    def L(self, base, exponent):
        if exponent == 1:
            return base
        if exponent == 2:
            return self.mat_mux(base, base)
        if exponent % 2 == 1:
            return self.mat_mux(base, self.L(base, exponent-1))
        else:
            result = self.L(base, exponent/2)
            return self.mat_mux(result, result)

    def mat_mux(self, A, B):
        if len(A) == 1 and len(B) == 1:
            return A * B
        C11 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        C12 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
        C21 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
        C22 = A[1][0] * B[0][1] + A[1][1] * B[1][1]
        return [[C11, C12], [C21, C22]]


if __name__ == '__main__':
    obj = Fibonacci()
    for i in range(100):
        print("fibPow("+str(i)+") =", obj.fibPow(i))
