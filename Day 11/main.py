from math import lcm


def main() -> None:
    with open("input.txt") as f:
        # Parsing input for monkey class constructor
        for monkey in [el.splitlines() for el in f.read().split("\n\n")]:

            items = [int(el) for el in monkey[1].removeprefix(
                "  Starting items: ").split(", ")]
            operation = monkey[2].removeprefix("  Operation: new = ")
            test = int(monkey[3].removeprefix("  Test: divisible by "))
            targets = (int(monkey[4].removeprefix("    If true: throw to monkey ")), int(
                monkey[5].removeprefix("    If false: throw to monkey ")))

            # Creating a monkey and adding it to the list
            Monkey.monkeys.append(Monkey(items, operation, test, targets))

        # Part 1 solution
        '''
        for _ in range(20):
            for monkey in Monkey.monkeys:
                monkey.inspectP1()
        '''

        # Part 2 solution
        for _ in range(10000):
            for monkey in Monkey.monkeys:
                monkey.inspectP2()

        # Prints monkeys
        # print("\n".join([el.__repr__() for el in Monkey.monkeys]))

        # Gets two monkeys with most inspected items and
        # prints the result of multiplication
        Monkey.monkeys.sort(key=lambda x: x.inspected, reverse=True)
        print(Monkey.monkeys[0].inspected * Monkey.monkeys[1].inspected)


class Monkey:
    """
    Object representation of monkey

    Static fields:
    Modulo (int) - LCM of all tests, used in formula (a mod kn) mod n = a mod n

    Monkeys (list[Monkey]) - list of all Monkeys

    Fields:
    Items (list[int]) - list of items currently held by the monkey

    Operation (str) - operation being performed on worry levels when monkey inspects items
    where old is old worry level, examples: "old * 5", "old * old", "old + 2"

    Test (int) - number item's worry level is tested against

    Targets (int, int) - throw target's index if item's worry level is divisible by test, target if otherwise

    Inspected (int) - counts how many items monkey has inspected

    Number (int) - monkey's order number, held for printing purposes

    Methods:
    InspectP1, InspectP2 - inspect methods for both parts of challenge

    ThrowTo (item, Monkey) - adds item to other monkey's item list (doesn't remove it from current item list)
    """
    modulo: int = 1
    monkeys: list["Monkey"] = []

    def __init__(self, startingItems: list[int], _operation: str, _test: int, _targets: tuple[int, int]) -> None:
        """
        StartingItems (list[int]) - starting items for monkey (a copy of the list is used)

        Operation (str) - operation being performed on worry levels when monkey inspects items
        where old is old worry level, examples: "old * 5", "old * old", "old + 2"

        Test (int) - number item's worry level is tested against

        Targets (int, int) - throw target's index if item's worry level is divisible by test, target if otherwise
        """
        self.items: list[int] = startingItems[::]
        # Example op: "old * 5"
        self.operation: str = _operation
        self.test: int = _test
        self.targets: tuple[int, int] = _targets

        # Monkey modulo must hold lcm of all monkey tests
        Monkey.modulo = lcm(Monkey.modulo, _test)

        # Initiates fields
        self.inspected: int = 0
        self.number = len(Monkey.monkeys)+1

    def inspectP1(self):
        for old in self.items:
            # Performs inspection, worry level decreases, performs modulo division on lcm of all monkey's tests
            new = (eval(self.operation)//3) % Monkey.modulo
            # Item inspected
            self.inspected += 1

            # Determines to which monkey item should be passed
            if new % self.test == 0:
                self.throwTo(new, self.targets[0])

            else:
                self.throwTo(new, self.targets[1])

        # All items has been inspected and thrown away
        self.items = []

    def inspectP2(self):
        for old in self.items:
            # Performs inspection, performs modulo division on lcm of all monkey's tests
            new = eval(self.operation) % Monkey.modulo
            # Item inspected
            self.inspected += 1

            # Determines to which monkey item should be passed
            if new % self.test == 0:
                self.throwTo(new, self.targets[0])

            else:
                self.throwTo(new, self.targets[1])

        # All items has been inspected and thrown away
        self.items = []

    def throwTo(self, item: int, monkey: int):
        Monkey.monkeys[monkey].items.append(item)

    def __repr__(self) -> str:
        return f"Monkey {self.number}:\n\t{self.items}\n\t{self.operation}\n\t{self.test} ? {self.targets[0]} : {self.targets[1]}"


if __name__ == "__main__":
    main()
