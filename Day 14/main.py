import cmath


def main() -> None:
    area: list[list[str]] = [["."]*500 for _ in range(500)]
    wallRange: list[list[int]] = [[len(area[0]), 0], [len(area), 0]]

    area[0][250] = "+"

    with open("input.txt") as f:
        for line in f.read().splitlines():
            line = [complex(*map(int, el.split(",")))
                    for el in line.split(" -> ")]

            for i, point in enumerate(line[1:], start=1):
                xStart, yStart = int(line[i-1].real), int(line[i-1].imag)
                xEnd, yEnd = int(point.real), int(point.imag)

                if xStart != xEnd:

                    if yStart < wallRange[1][0]:
                        wallRange[1][0] = yStart
                    if yStart > wallRange[1][1]:
                        wallRange[1][1] = yStart

                    for x in range(xStart, xEnd + 1 if xStart < xEnd else xEnd - 1, 1 if xStart < xEnd else -1):
                        x -= 250

                        if x < wallRange[0][0]:
                            wallRange[0][0] = x
                        if x > wallRange[0][1]:
                            wallRange[0][1] = x+1

                        area[yStart][x] = "#"

                else:
                    xStart -= 250

                    if xStart < wallRange[0][0]:
                        wallRange[0][0] = xStart
                    if xStart > wallRange[0][1]:
                        wallRange[0][1] = xStart+1

                    for y in range(yStart, yEnd + 1 if yStart < yEnd else yEnd - 1, 1 if yStart < yEnd else -1):

                        if y < wallRange[1][0]:
                            wallRange[1][0] = y
                        if y > wallRange[1][1]:
                            wallRange[1][1] = y

                        area[y][xStart] = "#"

    def printArea():
        print("  ", "".join(str(x % 10)
              for x in range(wallRange[0][1]-wallRange[0][0])))
        for y in range(0, wallRange[1][1]+1):
            print(str(y).zfill(3), "".join(
                area[y][wallRange[0][0]:wallRange[0][1]]))

    def spawnSand() -> bool:
        nonlocal wallRange
        x, y = 250, 0

        if area[0][250] == "o":
            return False

        while y < wallRange[1][1]:
            if area[y+1][x] == ".":
                y += 1

            elif area[y+1][x-1] == ".":
                x -= 1
                y += 1

            elif area[y+1][x+1] == ".":
                x += 1
                y += 1

            else:

                if x < wallRange[0][0]:
                    wallRange[0][0] = x-3
                if x > wallRange[0][1]:
                    wallRange[0][1] = x+3

                area[y][x] = "o"

                return True

        return False

    areaCopy: list[list[str]] = [[e for e in row] for row in area]

    grainsP1: int = 0

    printArea()
    while spawnSand():
        grainsP1 += 1

    printArea()
    print(grainsP1)

    grainsP2: int = 0

    area = areaCopy[::]
    wallRange[1][1] += 2
    area[wallRange[1][1]] = list("#"*500)

    while spawnSand():
        grainsP2 += 1

    printArea()
    print(grainsP2)


if __name__ == "__main__":
    main()
