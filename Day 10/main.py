def main() -> None:
    # Register X value
    value: int = 1
    # sum of strengths
    strSum: int = 0

    # Current drawing position
    x: int = 0
    y: int = 0
    # CRT image representation
    image: list[list[str]] = [list("."*40) for _ in range(6)]

    with open("input.txt") as f:

        cycle = 0
        for line in f.readlines():
            line = line.strip().split(" ")

            # Executes two cycles and adds to value
            if line[0] == "addx":
                #! Cycle begin
                x = cycle % 40
                cycle += 1
                # CRT draws the pixel
                image[y][x] = "#" if x in (value-1, value, value+1) else "."

                # Check for answer to p1
                if cycle in range(20, 221, 40):
                    strSum += cycle*value

                # If it's the end of line, move to the next one
                if x == 39:
                    y += 1
                #! Cycle end

                #! Cycle begin
                x = cycle % 40
                cycle += 1
                # CRT draws the pixel
                image[y][x] = "#" if x in (value-1, value, value+1) else "."

                # Check for answer to p1
                if cycle in range(20, 221, 40):
                    strSum += cycle*value

                # If it's the end of line, move to the next one
                if x == 39:
                    y += 1
                #! Cycle end

                # Executes command after two cycles
                value += int(line[1])

            # Executes one cycle
            elif line[0] == "noop":
                #! Cycle begin
                x = cycle % 40
                cycle += 1
                # CRT draws the pixel
                image[y][x] = "#" if x in (value-1, value, value+1) else "."

                # Check for answer to p1
                if cycle in range(20, 221, 40):
                    strSum += cycle*value

                # If it's the end of line, move to the next one
                if x == 39:
                    y += 1
                #! Cycle end

    print(strSum, "\n\n")
    print("\n".join("".join(el) for el in image))


if __name__ == "__main__":
    main()
