import os


def detect_unique_chars(inp: str, window_size: int) -> int:
    for i in range(0, len(inp) - window_size):
        window = [inp[x] for x in range(i, i + window_size)]
        if len(set(window)) == window_size:
            return i + window_size


def part_1(inp: str) -> int:
    return detect_unique_chars(inp, 4)


def part_2(inp: str) -> int:
    return detect_unique_chars(inp, 14)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    with open(f"../../../common/{os.path.split(os.getcwd())[-1]}/input.txt", "r") as fp:
        inp = fp.read()

    part_1_result = part_1(inp)
    print("part 1 result:", part_1_result)

    part_2_result = part_2(inp)
    print("part 2 result:", part_2_result)
