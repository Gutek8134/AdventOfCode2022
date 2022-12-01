def main() -> None:
    # Initializes the list
    calories: list = []
    # Opens the file
    with open("input.txt") as f:
        # Initializes temporary variable to store total amount of calories elf carries
        elf: int = 0

        for line in f.readlines():
            # If the line is the separator (\n), the amount of calories is appended to the list and temporary variable reset
            if line == "\n":
                calories.append(elf)
                elf = 0
                continue
            # If not, adds the calories to the total elf carries
            elf += int(line)
        # The last elf doesn't leave blank space, so it has to append at the end
        calories.append(elf)
    # Sorts the list in descending order
    calories.sort(reverse=True)

    # Prints maximum calories held by one elf
    print("Maximum: ", calories[0])
    # and total of the top 3
    print("Top 3:", sum(calories[0:3]))


if __name__ == "__main__":
    main()
