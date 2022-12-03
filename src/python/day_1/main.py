import os


def get_elves(inp: str) -> list[int]:
    return [sum(map(int, lines.split("\n"))) for lines in inp.split("\n\n")]


def part_1(inp: str) -> int:
    elves = get_elves(inp)
    return max(elves)


def part_2(inp: str) -> int:
    sorted_elves = sorted(get_elves(inp))
    return sum(sorted_elves[-3:])


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    with open(f"../../../common/{os.path.split(os.getcwd())[-1]}/input.txt", "r") as fp:
        inp = fp.read()

    part_1_result = part_1(inp)
    print("part 1 result:", part_1_result)

    part_2_result = part_2(inp)
    print("part 2 result:", part_2_result)
