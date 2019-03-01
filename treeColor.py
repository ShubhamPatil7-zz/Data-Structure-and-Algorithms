import turtle
import sys
import colorsys

WINDOW_SIZE = 600
BRANCHING_FACTOR = 3

SPEED = 0  # How fast to draw
BRANCH_MULTIPLY = .7


def getColor(depth, maxDepth):
    """Divides hue up based on maxDepth
	returns r,g,b
    """
    return colorsys.hsv_to_rgb((1 / maxDepth) * (depth), 1, .8)


def drawTree0(aTurtle, size):
    """ Draw a tree with 0 levels.
        (Does nothing.)
    """
    pass


def drawTree1(aTurtle, size):
    """ Draw a tree with 1 level.
        (Draws a single line of the size given.)
    """
    forward(size)
    backward(size)


def drawTree2(aTurtle, size):
    """ Draw a tree with 2 levels.
    """
    forward(size)
    left(BRANCH_ANGLE)
    forward(size / 2)
    backward(size / 2)
    right(2 * BRANCH_ANGLE)
    forward(size / 2)
    backward(size / 2)
    left(BRANCH_ANGLE)
    backward(size)


def drawTreeInit(aTurtle, segments, size):
    drawTree(aTurtle, segments, size, segments)


def drawTree(aTurtle, segments, size, maxSegments):
    """ Recursively draw a tree.

        :param aTurtle: the turtle to be used to do the drawing
        :param segments: non-negative integer
                    number of line segments from the base of the tree to
                    the end of any branch
        :param size: positive integer
                    length of tree trunk

        :pre: segments >= 0, size > 0.
              turtle is at base of tree,
              turtle is facing along trunk of tree,
              turtle is pen-down.

        :post: a segments-level tree was drawn on the canvas,
               turtle is at base of tree,
               turtle is facing along trunk of tree,
               turtle is pen-down.
    """
    if segments == 0:
        # base case: draw nothing
        pass
    else:
        # recursive case: draw trunk and two sub-trees

        # get color
        r, g, b = getColor(segments, maxSegments)
        # aTurtle.pencolor(COLOR[segments%len(COLOR)])
        aTurtle.pencolor(r, g, b)
        aTurtle.pensize(segments)

        aTurtle.forward(size)

        angleStep = 180 / (BRANCHING_FACTOR + 1)
        currAngle = angleStep

        for n in range(1, BRANCHING_FACTOR + 1):
            turnAngle = 90 - currAngle

            aTurtle.left(turnAngle)
            drawTree(aTurtle, segments - 1, size * BRANCH_MULTIPLY, maxSegments)
            aTurtle.right(turnAngle)
            currAngle += angleStep

        aTurtle.up()
        aTurtle.backward(size)
        aTurtle.down()

        r, g, b = getColor(segments, maxSegments)
        aTurtle.pensize(segments)
        # aTurtle.pencolor(COLOR[segments%len(COLOR)])
        aTurtle.pencolor(r, g, b)


MARGIN = 2  # Space at edges of canvas
PEN_SIZE = 2  # Thickness of turtle's pen


def initWorld(size):
    """ Initialize the drawing area.

        :param size: integer
                     length of tree trunk to draw
                     (not currently used)
        :pre: size > 0
        :post: coordinate system goes from
               (-2*size, -2*size) at lower-left
                 to (2*size, 2*size) at upper-right.
    """

    turtle.setup(WINDOW_SIZE, WINDOW_SIZE)

    # The lines below are removed because they keep one from
    # seeing the difference that the size parameter makes
    # in the perceived size of the tree.
    #
    # turtle.setworldcoordinates( -2*size - MARGIN, -2*size - MARGIN, \
    #                            2*size + MARGIN, 2*size + MARGIN )


def initTurtle(aTurtle):
    """ Set up the turtle by establishing the drawTree
        function's pre-conditions.

        :post: aTurtle is at origin ( center ),
               aTurtle is facing North,
               aTurtle's pen is down, size PEN_SIZE
    """
    aTurtle.speed(SPEED)
    aTurtle.up()

    aTurtle.home()  # turtle is at origin, facing east, pen-down
    aTurtle.goto(0, -WINDOW_SIZE / 2)  # no it isn't.
    aTurtle.left(90)  # turtle is facing North
    aTurtle.down()  # turtle's pen is put down
    aTurtle.pensize(PEN_SIZE)


def demo(segments, size=200):
    """ Print a message, initialize the world,
        draw an instance of the recursive tree, and wait for ENTER.

        segments: non-negative integer
                    number of line segments from the base of the tree to
                    the end of any branch
        size: positive integer
                    length of tree trunk
    """
    print("Drawing recursive tree with", (segments, size))
    initWorld(size)
    t = turtle.Turtle()
    initTurtle(t)
    drawTreeInit(t, segments, size)
    turtle.mainloop()


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        depth = int(sys.argv[1])
    demo(5)
