import os
from string import ascii_letters
from typing import TypeVar

T = TypeVar("T")


def chunks(lst: T, n: int) -> list[T]:
    return [lst[i : i + n] for i in range(0, len(lst), n)]


def get_character_score(char: str) -> int:
    return ascii_letters.index(char) + 1


def find_common_character(strings: list[str]) -> str:
    distinct_chars = {char for string in strings for char in string}
    return [char for char in distinct_chars if all(char in string for string in strings)][0]


def part_1(inp: str) -> int:
    rucksacks = inp.split("\n")
    score = 0
    for rucksack in rucksacks:
        score += get_character_score(find_common_character(chunks(rucksack, len(rucksack) // 2)))

    return score


def part_2(inp: str) -> int:
    lines = inp.split("\n")
    score = 0
    for group in chunks(lines, 3):
        score += get_character_score(find_common_character(group))

    return score


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    with open(f"../../../common/{os.path.split(os.getcwd())[-1]}/input.txt", "r") as fp:
        inp = fp.read()

    part_1_result = part_1(inp)
    print("part 1 result:", part_1_result)

    part_2_result = part_2(inp)
    print("part 2 result:", part_2_result)
