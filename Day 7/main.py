def main() -> None:
    with open("input.txt") as f:
        # Creates root directory and sets current directory to it
        Directory.root = Directory("/")
        currentDirectory: Directory = Directory.root

        for line in f.readlines():
            line = line.strip().split(" ")

            # Line is a command
            if line[0] == "$":
                # It's a cd command
                if line[1] == "cd":
                    # Directory exists as child of current one,
                    # current directory is changed to it
                    if currentDirectory.getDir(line[2]) is not None:
                        # Using toDir static method so (shitty) linter doesn't scream at me
                        currentDirectory = Directory.toDir(
                            currentDirectory.getDir(line[2]))

            # Line specifies existence of a directory
            elif line[0] == "dir":
                # It is added to CD children
                currentDirectory.addDir(line[1])
            # It's not a command or directory, so it's a file
            else:
                # Same as for directory
                currentDirectory.addFile(line[1], int(line[0]))

    # Uncomment if you want to see the whole tree
    # print(Directory.root.printTree())

    # Initializes values
    outcome: int = 0
    candidates: list[Directory] = []
    # Previously 30000000 - (70000000 - root size)
    requiredSpace: int = Directory.root.size - 40000000

    for dir in Directory.directories:
        # size is computed only once to quicken things a bit
        s = dir.size
        # Part 1 solution
        if s < 100000:
            outcome += dir.size
        # Part 2 solution
        if s >= requiredSpace:
            candidates.append(dir)

    print(outcome, min(candidates, key=lambda x: x.size).size)


class Directory:
    """
    Directory object

    Static methods:
    toDir (any): makes sure what you're using is a directory or throws an error,
    so linter doesn't scream at you

    Static fields:
    root (Directory): root directory, mother of all, parent set to self

    directories (list[Directory]): holds all of created directories to easily iterate over them

    Methods:

    Fields:
    Name (str): directory's name
    Parent (Directory): directory's parent, self for root
    Children (dict[str, Directory|File]): directory's children: files and other dirs
    """
    root: "Directory"
    # Holds all of the created directories
    directories: list["Directory"] = []

    # Shitty linter made me do this
    @staticmethod
    def toDir(obj) -> "Directory":
        if isinstance(obj, Directory):
            return obj
        raise TypeError(f"Object {obj} is not a directory")

    def __init__(self, _name: str, _parent: "Directory" = ..., **_children: "Directory|File") -> None:
        """
        Name (str): directory's name

        Parent (Directory): directory's parent, if not specified set to self

        Children (dict[str, Directory|File]): if you know them beforehand, you can set them with keywords (or splat a dict)
        """

        self.name = _name
        self.children: dict[str,
                            "Directory | File"] = _children if _children else {}
        # Sets parent to self for all children
        for child in self.children.values():
            child.parent = self

        # Sets parent to specified directory or self
        # I know you hate me for this
        if _parent != ...:
            self.parent: Directory = _parent
        else:
            self.parent = self

        # Adds self to the list
        Directory.directories.append(self)

    @property
    def size(self) -> int:
        """
        Size of all files in directory along with subdirectories' sizes
        """
        return sum(child.size for child in self.children.values())

    def getDir(self, name: str) -> "Directory | File | None":
        """
        Gets directory by name

        Name (str): name of the child dir or .. for parent dir or / for root
        """
        if name == "..":
            return self.parent
        elif name == "/":
            return Directory.root
        return self.children.get(name, None)

    def addDir(self, name: str):
        """
        Adds directory as a child of this one
        and sets its parent to self

        Name (str): name of the directory
        """
        self.children[name] = Directory(name, self)
        self.children[name].parent = self

    def addFile(self, name: str, size: int) -> None:
        """
        Adds file as a child of this one
        and sets its parent to self

        Name (str): name of the file
        Size (int): size of the file
        """
        self.children[name] = File(name, size)
        self.children[name].parent = self

    def __repr__(self) -> str:
        """
        Returns full path to the directory
        """
        if self.parent is self:
            return "/"
        return f"{self.parent.__repr__()}|{self.name}"

    def __str__(self) -> str:
        """
        Returns name of the directory
        """
        return self.name

    def printTree(self, n: int = 1) -> str:
        """
        Returns formatted view of the tree

        N (int): held for indentation purposes, don't change it
        """
        return f"{self.name}: {self.size}\n{4*n*' '}" + f"\n{4*n*' '}".join(str(child) if isinstance(child, File) else child.printTree(n+1) for child in self.children.values())


class File:
    """
    File object

    Fields:
    Name (str): name of the file
    Size (int): size of the file
    Parent (Directory): parent directory
    """

    def __init__(self, _name: str, _size: int) -> None:
        self.name = _name
        self.size: int = _size
        self.parent: Directory

    def __str__(self) -> str:
        return f"{self.name}: {self.size}"

    def __repr__(self) -> str:
        return str(self)


if __name__ == "__main__":
    main()
