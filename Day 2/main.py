def main1() -> None:
    total: int = 0
    with open("input.txt") as f:
        for line in f.readlines():
            # You choose rock
            if line[2] == "X":
                total += 1
                # Enemy chose rock
                if line[0] == "A":
                    total += 3
                # Enemy chose paper
                elif line[0] == "B":
                    total += 0
                # Enemy chose scissors
                elif line[0] == "C":
                    total += 6
            # You choose paper
            elif line[2] == "Y":
                total += 2
                # Enemy chose rock
                if line[0] == "A":
                    total += 6
                # Enemy chose paper
                elif line[0] == "B":
                    total += 3
                # Enemy chose scissors
                elif line[0] == "C":
                    total += 0
            # You choose scissors
            elif line[2] == "Z":
                total += 3
                # Enemy chose rock
                if line[0] == "A":
                    total += 0
                # Enemy chose paper
                elif line[0] == "B":
                    total += 6
                # Enemy chose scissors
                elif line[0] == "C":
                    total += 3

    print(total)


def main2() -> None:
    total: int = 0
    with open("input.txt") as f:
        for line in f.readlines():
            # You choose to lose
            if line[2] == "X":
                total += 0
                # Enemy chose rock, you choose scissors
                if line[0] == "A":
                    total += 3
                # Enemy chose paper, you choose rock
                elif line[0] == "B":
                    total += 1
                # Enemy chose scissors, you choose paper
                elif line[0] == "C":
                    total += 2
            # You choose to draw
            elif line[2] == "Y":
                total += 3
                # Enemy abd you chose rock
                if line[0] == "A":
                    total += 1
                # Enemy and you chose paper
                elif line[0] == "B":
                    total += 2
                # Enemy and you chose scissors
                elif line[0] == "C":
                    total += 3
            # You choose to win
            elif line[2] == "Z":
                total += 6
                # Enemy chose rock, you choose paper
                if line[0] == "A":
                    total += 2
                # Enemy chose paper, you choose scissors
                elif line[0] == "B":
                    total += 3
                # Enemy chose scissors, you choose rock
                elif line[0] == "C":
                    total += 1

    print(total)


if __name__ == "__main__":
    main1()
    main2()
