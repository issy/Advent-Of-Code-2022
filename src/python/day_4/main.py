import os
import re


def parse_lines(inp: str) -> list[tuple[set[int], set[int]]]:
    pattern = re.compile(r"^(\d+)-(\d+),(\d+)-(\d+)$")

    def parse_line(line: str) -> tuple[range, range]:
        match = pattern.match(line)
        if match is None:
            raise RuntimeError("Unable to parse line")

        nums = [int(match.group(i)) for i in range(1, 5)]

        return range(nums[0], nums[1] + 1), range(nums[2], nums[3] + 1)

    return [(set(i[0]), set(i[1])) for i in [parse_line(line) for line in inp.split("\n")]]


def check_intersection(line: tuple[set[int], set[int]]) -> bool:
    a, b = line
    intersection_size = len(a.intersection(b))
    return intersection_size in (len(a), len(b))


def part_1(inp: str) -> int:
    lines = parse_lines(inp)
    return len(list(filter(check_intersection, lines)))


def part_2(inp: str) -> int:
    lines = parse_lines(inp)
    return len(list(filter(bool, (a.intersection(b) for a, b in lines))))


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    with open(f"../../../common/{os.path.split(os.getcwd())[-1]}/input.txt", "r") as fp:
        inp = fp.read()

    part_1_result = part_1(inp)
    print("part 1 result:", part_1_result)

    part_2_result = part_2(inp)
    print("part 2 result:", part_2_result)
