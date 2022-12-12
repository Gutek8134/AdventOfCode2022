from collections import deque


def main():
    with open("input.txt") as f:
        area: Area = Area([list(el) for el in f.read().splitlines()])

    # Gets positions of S and E
    start, end = getTargets(area)

    # Changes S to a and E to z
    area.area[start[1]][start[0]] = "a"
    area.area[end[1]][end[0]] = "z"

    #! Using A* terminology

    # Initializes opened and closed lists
    opened: deque[Node] = deque([area.getElement(start[0], start[1])])
    closed: list[Node] = []

    # While opened is not empty
    while opened:
        # Gets q
        q: Node = opened.popleft()

        # For each q's successor
        for successor in q.successors:

            # Creates a Node object
            successor = area.getElement(successor[0], successor[1])

            # If its height is too big, element is skipped
            if successor.height > q.height + 1:
                continue

            # If element wasn't evaluated yet
            if successor not in closed:
                # Sets its g to parent's g + 1
                successor.g = q.g + 1
                # and adds to both closed and opened lists
                closed.append(successor)
                opened.append(successor)

    # Looks for endpoint and prints the answer
    for n in closed:
        if n == end:
            print("Part 1: ", n.g-1)

    # Initializes opened and closed lists
    opened: deque[Node] = deque([area.getElement(end[0], end[1])])
    closed: list[Node] = []

    # While opened is not empty
    while opened:
        # Gets q
        q: Node = opened.popleft()

        # For each q's successor
        for successor in q.successors:

            # Creates a Node object
            successor = area.getElement(successor[0], successor[1])

            # If its height is too low, element is skipped
            if successor.height < q.height - 1:
                continue

            # If element wasn't evaluated yet
            if successor not in closed:
                # Sets its g to parent's g + 1
                successor.g = q.g + 1
                # and adds to both closed and opened lists
                closed.append(successor)
                opened.append(successor)

    # Creates list of lowest points
    temp: list[Node] = []
    for n in closed:
        if n.height == 97:
            temp.append(n)

    # and prints the one closest to the endpoint
    print(min(temp, key=lambda x: x.g).g-1)


def getTargets(area: "Area") -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Gets S and E positions
    """
    # Initializes positions
    startPos: tuple[int, int] = (0, 0)
    stopPos: tuple[int, int] = (0, 0)

    # They both need to be found to return the values
    startFound, stopFound = False, False

    # For value for each column checks whether is it S or E
    # and if it is, writes down the position,
    # then if both were found returns
    for y, row in enumerate(area.getRows()):
        for x, el in enumerate(row):
            if el.value == "S":
                startPos = (x, y)
                startFound = True
                if startFound and stopFound:
                    return startPos, stopPos
            elif el.value == "E":
                stopPos = (x, y)
                stopFound = True
                if startFound and stopFound:
                    return startPos, stopPos
    raise Exception("WTF")


class Node:
    """
    Object representing a node in area

    Fields:
    X, Y (int) - node's position

    Value (str) - node's height value (a-z)

    G (int) - distance to start

    Height (int) - point's height (97-123 for a-z)

    Successors (list[tuple[int, int]]) - positions adjacent to the node's position

    H (int) - approximated distance to end (unused)

    F (int) - sum of G and H (unused)
    """

    def __init__(self, _x: int, _y: int, _value: str) -> None:
        self.x: int = _x
        self.y: int = _y
        self.value: str = _value
        self.g: int = 1
        self.h: int = 0
        self.parent: Node | None = None

    @property
    def f(self):
        return self.g

    @property
    def height(self) -> int:
        return ord(self.value)

    @property
    def successors(self) -> list[tuple[int, int]]:
        temp = []
        if self.x != 0:
            temp.append((self.x-1, self.y))
        if self.y != 0:
            temp.append((self.x, self.y-1))
        if self.x != Area.size[0]:
            temp.append((self.x+1, self.y))
        if self.y != Area.size[1]:
            temp.append((self.x, self.y+1))
        return temp

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Node):
            return __o.x == self.x and __o.y == self.y
        elif isinstance(__o, tuple):
            return __o[0] == self.x and __o[1] == self.y
        return False

    def __repr__(self) -> str:
        return f"Node({self.x}, {self.y}): {self.value}"


class Area:
    """
    Class representing an N x M area

    Static fields:
    Size (tuple[int, int]) - area's size (so I don't have to pass it to node.successors)

    Fields:
    Area (list[list[str]]) - area represented by 2d list of strings

    Methods:
    GetElement - returns Node at x,y

    GetRow - returns row of Nodes with set y

    GetColumn - returns column of Nodes with set x

    GetRows - returns list of all rows generated by GetRow

    GetColumns - returns list of all columns generated by GetColumn
    """
    size: tuple[int, int]

    def __init__(self, _area: list[list[str]]) -> None:
        self.area: list[list[str]] = _area
        Area.size = len(self.area[0])-1, len(self.area)-1

    def getElement(self, x: int, y: int) -> Node:
        return Node(x, y, self.area[y][x])

    def getRow(self, y: int) -> list[Node]:
        return [Node(x, y, el) for x, el in enumerate(self.area[y])]

    def getColumn(self, x: int) -> list[Node]:
        return [Node(x, y, row[x]) for y, row in enumerate(self.area)]

    def getRows(self) -> list[list[Node]]:
        return [self.getRow(i) for i in range(len(self.area))]

    def getColumns(self) -> list[list[Node]]:
        return [self.getColumn(i) for i in range(len(self.area[0]))]

    def __iter__(self):
        yield from self.area.__iter__()

    def __repr__(self) -> str:
        return "\n".join([el.__repr__() for el in self])


if __name__ == "__main__":
    main()
