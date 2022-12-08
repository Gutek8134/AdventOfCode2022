def main() -> None:
    trees: list[list[Tree]] = []
    with open("input.txt") as f:
        for x, line in enumerate(f.readlines()):
            line = line.strip()
            temp: list[Tree] = []
            for y, ch in enumerate(line):
                temp.append(Tree(x, y, int(ch)))
            trees.append(temp)

    visible: int = 0
    scores: list[int] = []
    for row in trees:
        for tree in row:
            if tree.isVisible(trees):
                visible += 1
            scores.append(tree.viewScore(trees))
    print(visible, max(scores))


class Tree:
    """
    Object representation of tree and its position

    Parameters:
    x, y (int) - position indexes
    height (int) - tree height


    Methods:

    isVisible (tree area) - checks if the tree is visible from outside and returns the outcome

    viewScore (tree area) - returns tree's view score, calculated by multiplying
    the number of other trees visible in 4 directions
    """

    def __init__(self, _x: int, _y: int, _height: int) -> None:
        """
        X, Y (int) - position of the tree

        Height (int) - height of the tree
        """
        self.x: int = _x
        self.y: int = _y
        self.height: int = _height

    def isVisible(self, trees: list[list["Tree"]]) -> bool:
        """
        Trees (list[list[Tree]]): 2d list of trees

        Returns whether the tree is visible from the outside
        """
        # Tree is always visible from the outside if it is on the edge
        if self.x in (0, len(trees)-1) or self.y in (0, len(trees)-1):
            return True

        return all(tree.height < self.height for tree in trees[self.x][self.y+1:]) or\
            all(tree.height < self.height for tree in trees[self.x][:self.y]) or\
            all(el[self.y].height < self.height for el in trees[self.x+1:]) or\
            all(el[self.y].height < self.height for el in trees[:self.x])

    def viewScore(self, trees: list[list["Tree"]]) -> int:
        """
        Trees (list[list[Tree]]): 2d list of trees

        Returns tree's view score
        """
        # scores: [left, top, right, bottom]
        scores: list[int] = [0, 0, 0, 0]
        if self.x in (0, len(trees)-1) or self.y in (0, len(trees)-1):
            return 0

        # Trees to the left
        for tree in trees[self.x][self.y-1::-1]:
            scores[0] += 1
            if tree.height >= self.height:
                break

        # Trees to the top
        for el in trees[self.x-1::-1]:
            tree = el[self.y]
            scores[1] += 1
            if tree.height >= self.height:
                break

        # Trees to the right
        for tree in trees[self.x][self.y+1:]:
            scores[2] += 1
            if tree.height >= self.height:
                break

        # Trees to the bottom
        for el in trees[self.x+1:]:
            tree = el[self.y]
            scores[3] += 1
            if tree.height >= self.height:
                break

        return scores[0] * scores[1] * scores[2] * scores[3]

    def __repr__(self) -> str:
        return str(self.height)


if __name__ == "__main__":
    main()
