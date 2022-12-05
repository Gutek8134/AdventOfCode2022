def main() -> None:
    # Initializes list for crates and commands
    crates: list[list[str]]
    # Command format: number of crates, index column_from, index column_to
    commands: list[tuple[int, int, int]] = []

    with open("input.txt") as f:
        # Shorthand and a copy
        lines = f.readlines()
        # It's needed to properly use input and create crates list
        height, width = getSizes(lines)
        # Creating crates list
        crates = [[] for _ in range(width)]
        # Converts input of crates to a 2d list
        for line in lines[:height]:
            # 1- first letter, then every four characters
            for i in range(1, len(line), 4):
                # Some places are empty, holding a "   "
                if line[i].isalpha():
                    # Floor division says exactly where the crate belongs
                    crates[i//4].insert(0, line[i])

        # Formats command lines
        for line in lines[height+2:]:
            commands.append(tuple(map(int, line.strip().split(" ")[1::2])))

    # Initializes stacks with their copies
    stacks: list[stack] = [stack(crate) for crate in crates]
    stacksC: list[stack] = [stack(crate) for crate in crates]

    # Runs the commands
    for command in commands:
        stacks[command[1]-1].moveTo(stacks[command[2]-1], command[0])
        stacksC[command[1]-1].moveTo9001(stacksC[command[2]-1], command[0])

    # Prints the output
    print("".join(tuple(map(lambda x: x.values[-1], stacks))), "".join(tuple(
        map(lambda x: x.values[-1], stacksC))), sep="\n")


# Gets height and width of crates "image"
def getSizes(lines: list[str]) -> tuple[int, int]:
    for i, l in enumerate(lines):
        if l[1] == "1":
            return i, int(l[-3])
    return 0, 0


# Custom class for crate stack
class stack:
    # Initializes itself to a list
    # [::] makes a copy of the list, because it caused major bugs
    def __init__(self, values: list[str]) -> None:
        self.values: list[str] = values[::]

    # Pops last n elements and returns tuple of them
    def get(self, n=1) -> tuple[str]:
        return tuple(self.values.pop() for _ in range(n))

    # Same but with the same order
    def get9001(self, n=1) -> tuple[str]:
        return tuple(self.values.pop() for _ in range(n))[::-1]

    # Adds values to the stack
    def add(self, *_values: str) -> None:
        for value in _values:
            self.values.append(value)

    # Moves a number of crates to another stack
    # "stack" is used, because the class itself is not present in the scope
    def moveTo(self, other: "stack", number=1) -> None:
        other.add(*self.get(number))

    # Same but with the same order
    def moveTo9001(self, other: "stack", number=1) -> None:
        other.add(*self.get9001(number))

    # In case stack needs to be printed
    def __repr__(self) -> str:
        return self.values.__repr__()


if __name__ == "__main__":
    main()
