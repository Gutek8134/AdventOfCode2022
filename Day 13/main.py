def main():
    with open("input.txt", "r") as f:
        # Saves input in manner [["[...]","[...]"], ...]
        trees: list[list[str]] = [el.splitlines()
                                  for el in f.read().split("\n\n")]

    # Initializes list of trees and solution
    treesList: list[Tree] = [Tree([[2]]), Tree([[6]])]
    s: int = 0
    # For left and right tree (they come in pairs)
    for i, (left, right) in enumerate(trees, start=1):
        # Parse them to Tree instances
        left, right = Tree(eval(left)), Tree(eval(right))
        # Add to list of trees
        treesList.extend((left, right))
        # If they are in correct order, add index to solution
        if left < right:
            s += i

    treesList.sort()
    # Initializes distress to 1 due to multiplication instead of summing
    distress = 1
    for i, tree in enumerate(treesList, start=1):
        # Looks for [[2]] and [[6]], then multiplies their indexes
        if tree == Tree([[2]]) or tree == Tree([[6]]):
            distress *= i

    # Print solution
    print(s)
    print(distress)


class Tree:
    """
    Class representing the the whole tree as well as its nodes

    Fields:
    Children (list[int | Tree]) - holds node's children
    """

    def __init__(self, values: list[list | int]) -> None:
        # Initializes field
        self.children: list[int | Tree] = []
        # If value is a list, it's converted to Tree, else just added to children
        for value in values:
            if isinstance(value, list):
                self.children.append(Tree(value))
            else:
                self.children.append(value)

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Tree):
            assert isinstance(other, Tree)
            # Tree is less than other tree when the first different child
            # is lesser then the other or its children are a subset
            # of other tree's children
            for l, r in zip(self.children, other.children):

                # If only one child is a Tree, other is converted
                if isinstance(l, Tree) and isinstance(r, int):
                    r = Tree([r])

                elif isinstance(l, int) and isinstance(r, Tree):
                    l = Tree([l])

                if l < r:
                    return True
                elif l > r:
                    return False

            return len(self.children) < len(other.children)

        elif isinstance(other, int):
            # Tree is less than an int when
            # its first child is lesser than the int
            assert isinstance(other, int)
            return self < Tree([other])

        # In case other object is neither Tree or int, False is returned
        return False

    def __eq__(self, __o: object) -> bool:
        # Tree is equal to other object when other object
        # is also a Tree and their children lists are equal
        if isinstance(__o, Tree):
            return self.children == __o.children
        return False

    def __repr__(self) -> str:
        return "Tree: " + self.children.__repr__()


if __name__ == "__main__":
    main()
