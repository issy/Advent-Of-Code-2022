import os
import re


def parse_lines(inp: str) -> tuple[dict[str, list[str]], list[tuple[int, str, str]]]:
    lines = inp.split("\n")
    break_index = 0
    for index, line in enumerate(lines):
        if line == "":
            break_index = index
            break

    crate_lines = lines[:break_index]
    instruction_lines = lines[break_index + 1:]

    crates = {}
    for index, crate_key in enumerate(crate_lines.pop()[1::4]):
        stack = []
        for line in crate_lines[::-1]:
            try:
                crate = line[1::4][index]
            except IndexError:
                continue
            if crate != " ":
                stack.append(crate)

        crates[crate_key] = stack

    instruction_pattern = re.compile(r"^move (\d+) from (\d+) to (\d+)$")
    instructions = []
    for line in instruction_lines:
        match = instruction_pattern.match(line)
        instructions.append((int(match.group(1)), match.group(2), match.group(3)))

    return crates, instructions


def move_crates(
    crates: dict[str, list[str]],
    instructions: list[tuple[int, str, str]],
    *,
    keep_order: bool = False
) -> str:
    for quantity, from_stack, to_stack in instructions:
        from_stack = crates[from_stack]
        to_stack = crates[to_stack]
        buffer = [from_stack.pop() for _ in range(quantity)]
        if keep_order:
            buffer.reverse()

        for crate in buffer:
            to_stack.append(crate)

    return "".join(crates[stack][-1] for stack in crates)


def part_1(inp: str) -> str:
    crates, instructions = parse_lines(inp)
    return move_crates(crates, instructions)


def part_2(inp: str) -> str:
    crates, instructions = parse_lines(inp)
    return move_crates(crates, instructions, keep_order=True)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    with open(f"../../../common/{os.path.split(os.getcwd())[-1]}/input.txt", "r") as fp:
        inp = fp.read()

    part_1_result = part_1(inp)
    print("part 1 result:", part_1_result)

    part_2_result = part_2(inp)
    print("part 2 result:", part_2_result)
