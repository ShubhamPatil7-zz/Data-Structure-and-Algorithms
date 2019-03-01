from turtle import *
import math


def draw_rectangles(levels, size=100):
    length = size
    width = length / 1.618
    sum = 0.0

    if levels == 0:
        pass

    if levels >= 1:
        up()
        fd(length / 2)
        down()
        left(90)
        fd(width / 2)
        left(90)
        fd(length)
        left(90)
        fd(width)
        left(90)
        fd(length)
        left(90)
        fd(width / 2)
        left(90)
        up()
        fd(length / 2)
        left(180)
        left(90)
        sum += 2 * (length + width) + draw_rectangles(levels - 1, width)
    return sum


def init(size):
    setworldcoordinates(-size, -size, size + 100, size + 100)
    speed(0)
    down()


def main():
    levels = int(input("Enter the number of levels\n"))
    size = int(input("Enter the size the long edge\n"))
    init(size)
    print("Summation of all sides: ", math.ceil(draw_rectangles(levels, size)))
    mainloop()


if __name__ == '__main__':
    main()
