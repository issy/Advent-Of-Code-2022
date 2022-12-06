import os


def part_1(inp: str) -> int:
    for i in range(0, len(inp) - 4):
        window = [inp[x] for x in range(i, i + 4)]
        if len(set(window)) == 4:
            return i + 1


def part_2(inp: str) -> None:
    ...


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    with open(f"../../../common/{os.path.split(os.getcwd())[-1]}/input.txt", "r") as fp:
        inp = fp.read()

    part_1_result = part_1(inp)
    print("part 1 result:", part_1_result)

    part_2_result = part_2(inp)
    print("part 2 result:", part_2_result)
