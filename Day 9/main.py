def main() -> None:
    # Creates two ropes for two parts of the challenge
    rope1: Rope = Rope(2)
    rope2: Rope = Rope(10)

    with open("input.txt") as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            # Performs commands
            rope1.move(line[0], int(line[1]))
            rope2.move(line[0], int(line[1]))

    # Prints result
    print(len(rope1.touched), len(rope2.touched))


class Part:
    """
    Object representing one part of a rope

    Fields:
    X, Y (int) - position

    Methods:
    Touches (Part)->bool - returns whether one rope part is touching another

    Move (str dir, int n) - moves the part by n in one of four directions: Up, Down, Left, Right,
    dir being the first letter

    Change Pos (x,y) - changes part's position to x,y
    """

    def __init__(self, _x: int, _y) -> None:
        self.x: int = _x
        self.y: int = _y

    def touches(self, other: "Part") -> bool:
        """
        Returns whether one rope part is touching another (8-directional + the same position)

        Parameters:

        Other - another part of a rope
        """
        # Checks in 8 directions
        return self.x in (other.x, other.x-1, other.x+1) and self.y in (other.y, other.y-1, other.y+1)

    def move(self, dir: str, n: int = 1) -> None:
        """
        Moves the part by n in one of four directions: Up, Down, Left, Right,
        dir being the first letter

        Parameters:

        Dir - direction expressed by U(p), D(own), L(eft) or R(ight)

        N - number of spaces to move
        """
        # I know i could use a dict[str, tuple[int, int]]
        if dir.upper() == "L":
            self.x -= n
        elif dir.upper() == "U":
            self.y += n
        elif dir.upper() == "R":
            self.x += n
        elif dir.upper() == "D":
            self.y -= n

    def changePos(self, x: int, y: int) -> None:
        """
        Changes part's position to x,y

        Parameters:

        X, Y - position indexes
        """
        self.x, self.y = x, y

    def __repr__(self) -> str:
        # Represents self as position
        return f"({self.x}, {self.y})"


class Rope:
    """
    Represents a ful rope with its ability to move

    Fields:
    Parts (list[Part]) - holds all parts of the rope

    Touched (set[tuple[int, int]]) - holds all parts touched by the tail

    Head, Tail (Part) - first and last part of the rope

    Methods:

    Move (str dir, int n) - moves the head by n in dir, and other parts if needed
    """

    def __init__(self, n: int = 2) -> None:
        """
        Parameters:

        N - number of parts in the rope
        """
        self.parts: list[Part] = [Part(0, 0) for _ in range(n)]
        self.touched: set[tuple[int, int]] = {(0, 0)}

    def move(self, dir: str, n: int = 1) -> None:
        """
        Moves the head by n in dir, and other parts if needed

        Parameters:

        Dir - direction expressed by U(p), D(own), L(eft) or R(ight)

        N - number of spaces to move
        """
        # Move once at a time
        for _ in range(n):
            # Moves head
            self.head.move(dir)
            # Each part of rope must be connected to the one before it
            for index, part in enumerate(self.parts[1:], start=0):
                if not part.touches(self.parts[index]):
                    _x, _y = part.x, part.y
                    other: Part = self.parts[index]

                    if other.x > _x:
                        _x += 1
                    elif other.x < _x:
                        _x -= 1

                    if other.y > _y:
                        _y += 1
                    elif other.y < _y:
                        _y -= 1

                    part.changePos(_x, _y)

            # Adds current tail's position to the set, which's length is the answer to the challenge
            self.touched.add((self.tail.x, self.tail.y))

    @property
    def head(self) -> Part:
        return self.parts[0]

    @property
    def tail(self) -> Part:
        return self.parts[-1]

    def __repr__(self) -> str:
        return ", ".join(map(lambda x: x.__repr__(), self.parts))


if __name__ == "__main__":
    main()
