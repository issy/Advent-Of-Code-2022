import os
from string import ascii_letters


def part_1(inp: str) -> int:
    rucksacks = inp.split("\n")
    score = 0
    for rucksack in rucksacks:
        intersection = len(rucksack) // 2
        first_half = rucksack[:intersection]
        second_half = rucksack[intersection:]
        (duplicate_letter,) = tuple({
            letter for letter in rucksack
            if letter in first_half
            and letter in second_half
        })
        score += ascii_letters.index(duplicate_letter) + 1

    return score


def part_2(inp: str) -> int:
    lines = inp.split("\n")
    groups = [lines[i:i + 3] for i in range(0, len(lines), 3)]
    score = 0
    for group in groups:
        all_distinct_letters = {letter for elf in group for letter in elf}
        (shared_letter,) = [letter for letter in all_distinct_letters if all(letter in elf for elf in group)]
        score += ascii_letters.index(shared_letter) + 1

    return score


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    with open(f"../../../common/{os.path.split(os.getcwd())[-1]}/input.txt", "r") as fp:
        inp = fp.read()

    part_1_result = part_1(inp)
    print("part 1 result:", part_1_result)

    part_2_result = part_2(inp)
    print("part 2 result:", part_2_result)
