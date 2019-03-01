import turtle

BRANCH_ANGLE = 45  # causes right angle between two branches
SPEED = 6  # How fast to draw


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


def drawTree(aTurtle, segments, size):
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
        aTurtle.forward(size)
        aTurtle.left(BRANCH_ANGLE)
        drawTree(aTurtle, segments - 1, size / 2)
        aTurtle.right(2 * BRANCH_ANGLE)
        drawTree(aTurtle, segments - 1, size / 2)
        aTurtle.left(BRANCH_ANGLE)
        aTurtle.backward(size)


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

    turtle.setup(600, 600)

    # The lines below are removed because they keep one from
    # seeing the difference that the size parameter makes
    # in the perceived size of the tree.
    #
    # turtle.setworldcoordinates( -2*size - MARGIN, -2*size - MARGIN,
    #                            2*size + MARGIN, 2*size + MARGIN )


def initTurtle(aTurtle):
    """ Set up the turtle by establishing the drawTree
        function's pre-conditions.

        :post: aTurtle is at origin ( center ),
               aTurtle is facing North,
               aTurtle's pen is down, size PEN_SIZE
    """
    aTurtle.speed(SPEED)
    aTurtle.home()  # turtle is at origin, facing east, pen-down
    aTurtle.left(90)  # turtle is facing North
    aTurtle.down()  # turtle's pen is put down
    aTurtle.pensize(PEN_SIZE)


def demo(segments, size=100):
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
    drawTree(t, segments, size)
    turtle.mainloop()


demo(7, 150)
