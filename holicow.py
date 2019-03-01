"""
CSCI-603 Lab 9(Holi Cow)
Author: Indrajeet Vidhate
Author: Shubham Patil
"""

import sys
import math


class CowNode:
    """
    Node Class for the cows.
    """
    __slots__ = 'name', 'X', 'Y', 'color', 'neighbors', 'colorsTriggered'

    def __init__(self, name, X, Y):
        self.name = name
        self.X = int(X)
        self.Y = int(Y)
        self.color = []
        self.neighbors = []
        self.colorsTriggered = {}

    def neighborList(self):
        """
        Adjancency List for Cows
        :return:
        """
        connectedTo = []
        for x in self.neighbors:
            connectedTo.append(x.name)
        return connectedTo

    def __str__(self):
        return self.name


class PaintballNode:
    """
    Node Class for the Paint-balls
    """
    __slots__ = 'name', 'X', 'Y', 'radius', 'neighbors', 'directNeighbors'

    def __init__(self, name, X, Y, radius):
        self.name = name
        self.X = int(X)
        self.Y = int(Y)
        self.radius = int(radius)
        self.neighbors = []
        self.directNeighbors = []

    def addNeighbor(self, neighbor):
        """
        Adds given node to adjecency list of Paint-ball
        :param neighbor: Node to be added to Adjacency List
        :return:
        """
        if isinstance(neighbor, CowNode):
            self.neighbors.append(neighbor)
            self.directNeighbors.append(neighbor)
        else:
            self.neighbors.append(neighbor)
            self.directNeighbors.append(neighbor)
            for x in neighbor.neighbors:
                if x not in self.neighbors:
                    self.neighbors.append(x)

    def neighborList(self):
        """
        Adjacency List of the Paint-ball
        :return:
        """
        connectedTo = []
        for x in self.directNeighbors:
            connectedTo.append(x.name)
        return connectedTo

    def trigger(self, visited=None):
        """
        Triggers the paintball and paints cows within it's range and
        triggers other paintballs within it's range.
        :param visited:
        :return:
        """
        count = 0
        if visited is None:
            visited = []
            visited.append(self)

        for x in self.directNeighbors:
            if x not in visited:
                if isinstance(x, CowNode):
                    print("\t", x.name, "is painted", self.name)
                    count += 1
                if isinstance(x, PaintballNode):
                    print("\t", x.name, "Paintball is triggered by", self.name, "Paintball!")
                    count += x.trigger(visited)
        return count

    def winner_result(self, visited=None):
        """
        To identify chain reaction caused by best choice paint-ball.
        :param visited:
        :return:
        """
        if visited is None:
            visited = []
            visited.append(self)

        for x in self.directNeighbors:
            if x not in visited:
                if isinstance(x, CowNode):
                    x.color.append(self.name)
                if isinstance(x, PaintballNode):
                    x.winner_result(visited)

    def __str__(self):
        return self.name


class Graph:
    """
    Class to generate Graph for CowNodes and PaintballNodes
    """
    __slots__ = 'fieldInfo', 'colorCount'

    def __init__(self):
        self.fieldInfo = {}
        self.colorCount = {}

    def in_range(self, Obj1, Obj2):
        """
        tells whether two nodes are within range of each other.
        :param Obj1: Must be PaintballNode
        :param Obj2: Can be CowNode or PaintballNode
        :return: true if given Obj2 is within reach of Obj1
        """
        x1 = Obj1.X
        y1 = Obj1.Y
        x2 = Obj2.X
        y2 = Obj2.Y
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance <= Obj1.radius

    def addCowNode(self, name, X, Y):
        """
        Adds the CowNode to the Graph and Adjacency List of Paintballs
        for which they are in range.
        :param name: Name of the Cow
        :param X: x co-ordinate of CowNode
        :param Y: y co-ordinate of CowNode
        :return:
        """
        self.fieldInfo[name] = CowNode(name, X, Y)
        for x in self.fieldInfo:
            if not x == name and isinstance(self.fieldInfo[x], PaintballNode):
                if self.in_range(self.fieldInfo[x], self.fieldInfo[name]):
                    self.fieldInfo[x].addNeighbor(self.fieldInfo[name])

    def addPaintballNode(self, name, X, Y, radius):
        """
        Adds the PaintballNode to the Graph and Adjacency List of Paintballs
        for which they are in range.
        :param name: Color of Paintball
        :param X: x co-ordinate of PaintballNode
        :param Y: y co-ordinate of PaintballNode
        :param radius: radius of PaintballNode
        :return:
        """
        self.fieldInfo[name] = PaintballNode(name, X, Y, radius)
        for x in self.fieldInfo:
            if not x == name:
                if isinstance(self.fieldInfo[x], CowNode):
                    if self.in_range(self.fieldInfo[name], self.fieldInfo[x]):
                        self.fieldInfo[name].addNeighbor(self.fieldInfo[x])
                else:
                    if self.in_range(self.fieldInfo[name], self.fieldInfo[x]):
                        self.fieldInfo[name].addNeighbor(self.fieldInfo[x])
                    elif self.in_range(self.fieldInfo[x], self.fieldInfo[name]):
                        self.fieldInfo[x].addNeighbor(self.fieldInfo[name])

    def simulate(self):
        """
        Triggers all the paintballs in the Field(Graph)
        :return:
        """
        for x in self.fieldInfo:
            if isinstance(self.fieldInfo[x], PaintballNode):
                print("Triggering", x, "Paintball")
                self.colorCount[x] = self.fieldInfo[x].trigger()

    def displayColor(self):
        """
        Displays the Colors painted on Cows after triggering Paint-ball
        :return:
        """
        for x in self.fieldInfo:
            if isinstance(self.fieldInfo[x], CowNode):
                print(x + "'s color's:", self.fieldInfo[x].color)

    def result(self):
        """
        Displays the best choice paint-ball along with number of
        colors painted cows due to triggering of that paintball.
        :return: max : number of cows painted due to triggering,
                 color: The best choice Paintball
        """
        max = 0
        for x in self.colorCount:
            if self.colorCount[x] > max:
                max = self.colorCount[x]
                color = x
        if not max == 0:
            self.fieldInfo[color].winner_result()
            return max, color
        else:
            return 0, 0


def main():
    """
    Reads the Field(Graph) input from file and generates the
    Graph and simulates triggering of paint-balls.
    :return:
    """
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        print("Usage: holicow.py <FileName>")
    field = Graph()
    with open(file_name) as f:
        for line in f:
            line.strip()
            entry = line.split()
            if entry[0] == 'cow':
                field.addCowNode(entry[1], entry[2], entry[3])

            if entry[0] == 'paintball':
                field.addPaintballNode(entry[1], entry[2], entry[3], entry[4])

    print("Field of Dreams")
    print("---------------")
    for nodes in field.fieldInfo:
        print(nodes, " connected to ", field.fieldInfo[nodes].neighborList())

    print("Beginning Simulation...")
    field.simulate()

    print("Results:")
    max, color = field.result()
    if max > 0:
        print("Triggering the", color, "paint-ball is the best choice with", max, "total paint on cows.")
        field.displayColor()
    else:
        print("No cows were printed were painted by any starting paint-ball!")


if __name__ == '__main__':
    main()
