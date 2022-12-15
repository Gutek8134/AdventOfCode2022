import re


def main() -> None:
    # Used to switch between test case and real one
    TestY: int = 2000000

    # Holds beginnings and ends of sensor areas at TestY
    lines: list[tuple[int, int]] = []
    # Set of beacon positions
    beacons: set[tuple[int, int]] = set()

    # Holds radius for each sensor
    sensorRads: dict[complex, int] = {}

    with open("input.txt") as f:
        for match in re.findall(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", f.read()):
            # Converts input data to coordinates of sensor and beacon
            sensor, beacon = complex(int(match[0]), int(match[1])),\
                complex(int(match[2]), int(match[3]))

            # Adds sensing radius to the dict
            sensorRads[sensor] = dist(sensor, beacon)

            # Beacon is at TestY coord, so it's added to the set
            if int(match[3]) == TestY:
                beacons.add((int(match[2]), int(match[3])))

            # Length of the line sensor area creates at TestY
            length = dist(sensor, beacon) - abs(sensor.imag - TestY)
            # If it exists, it is added to the list
            if length >= 0:
                lines.append((int(sensor.real-length),
                             int(sensor.real+length)))

    # Creates sets consisting of ranges determined by lines and removes known beacon locations
    # Answer to p1 is the number of elements in the final set
    print(len(set.union(*(set(range(start, stop+1))
          for start, stop in lines))-set(y for x, y in beacons)))

    # Creates edges of the sensor areas
    testRows: set[int] = set()
    testColumns: set[int] = set()
    for coord, rad in sensorRads.items():
        testRows.add(int(coord.imag - coord.real + rad + 1))
        testRows.add(int(coord.imag - coord.real - rad - 1))
        testColumns.add(int(coord.imag + coord.real + rad + 1))
        testColumns.add(int(coord.imag + coord.real - rad - 1))

    # For each element in the edge
    for x in testRows:
        for y in testColumns:
            testPoint: complex = complex((y-x)//2, (y+x)//2)

            # If it's in bounds
            if 0 <= testPoint.real <= 4000000 and 0 <= testPoint.imag <= 4000000:
                # and its distance to every sensor is lesser than its radius
                if all(dist(testPoint, sensorPos) > sensorRad for sensorPos, sensorRad in sensorRads.items()):
                    # it's what we're looking for and answer is printed
                    print(int(testPoint.real * 4000000 + testPoint.imag))


def dist(a: complex, b: complex) -> int:
    """Manhattan distance between two points with complex coords"""
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))


if __name__ == "__main__":
    main()
