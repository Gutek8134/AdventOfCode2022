def main() -> None:
    with open("input.txt") as f:
        # Initializes buffer
        chars: list[str] = []
        # These two hold whether packet start was found
        packet: bool = False

        for pos, char in enumerate(f.read(), start=1):
            # If current character is in the buffer/list, chars is set to not hold it anymore
            if char in chars:
                chars = chars[chars.index(char)+1:]
            # Adds character to the list
            chars.append(char)

            # Checks the length of the list that is sure to hold unique values
            # If it is big enough, the current position is printed
            if len(chars) == 4 and not packet:
                print("Start of packet:", pos)
                packet = True
            elif len(chars) == 14:
                print("Start of message:", pos)
                return


if __name__ == "__main__":
    main()
