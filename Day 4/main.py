def main() -> None:
    # Initializing outcome variables
    containingPairs: int = 0
    overlappingPairs: int = 0
    with open("input.txt") as f:
        for line in f.readlines():
            # Changing "n-n,n-n" format to ((n,n), (n,n))
            line = tuple(
                map(lambda x: tuple(map(int, x.split("-"))), line.split(",")))

            # Splat operator, oh yeah!
            if rangeOverlaps(*line):
                overlappingPairs += 1

            if rangeContains(*line):
                containingPairs += 1

    print(containingPairs, overlappingPairs)


# Range contains another when smaller index of one is larger than the other
# and greater index is smaller than another
def rangeContains(range1: tuple[int, int], range2: tuple[int, int]) -> bool:
    return (range1[0] >= range2[0] and range1[1] <= range2[1]) or (range1[0] <= range2[0] and range1[1] >= range2[1])


# Ranges overlap when one end of any range is between the other range's ends
def rangeOverlaps(range1: tuple[int, int], range2: tuple[int, int]) -> bool:
    return range2[0] <= range1[0] <= range2[1] or range2[0] <= range1[1] <= range2[1]\
        or range1[0] <= range2[0] <= range1[1] or range1[0] <= range2[1] <= range1[1]


if __name__ == "__main__":
    main()
