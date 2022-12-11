import math
import os
from typing import Callable, TypeVar

T = TypeVar("T")


class Grid:
    grid: list[list[int]]
    x_size: int
    y_size: int

    def __init__(self, inp: str):
        self.grid = [[int(i) for i in line] for line in inp.splitlines()]
        self.x_size = len(self.grid)
        self.y_size = len(self.grid[0])

    def get_cell(self, x: int, y: int) -> int:
        return self.grid[x][y]

    def cell_is_visible(self, x: int, y: int) -> bool:
        cell_height = self.get_cell(x, y)

        def check(cell: int) -> bool:
            return cell < cell_height

        if x in [0, self.x_size - 1] or y in [0, self.y_size - 1]:  # Edges of grid
            return True

        for r in [range(x), range(x + 1, self.x_size)]:  # Left/right
            if all([check(self.get_cell(check_x, y)) for check_x in r]):
                return True

        for r in [range(y), range(y + 1, self.y_size)]:  # Left/right
            if all([check(self.get_cell(x, check_y)) for check_y in r]):
                return True

        return False

    def get_scenic_score(self, x: int, y: int) -> int:
        cell_height = self.get_cell(x, y)

        def check(cell: int) -> bool:
            return cell < cell_height

        scores = []
        score = 0
        for check_x in range(x - 1, -1, -1):
            score += 1
            cell = self.get_cell(check_x, y)
            if not check(cell):
                break

        scores.append(score)
        score = 0
        for check_x in range(x + 1, self.x_size):
            score += 1
            cell = self.get_cell(check_x, y)
            if not check(cell):
                break

        scores.append(score)
        score = 0
        for check_y in range(y - 1, -1, -1):
            score += 1
            cell = self.get_cell(x, check_y)
            if not check(cell):
                break

        scores.append(score)
        score = 0
        for check_y in range(y + 1, self.y_size):
            score += 1
            cell = self.get_cell(x, check_y)
            if not check(cell):
                break

        scores.append(score)
        return math.prod(scores)

    def map(self, fn: Callable[[int, int], T]) -> list[T]:
        return [fn(x, y) for x in range(self.x_size) for y in range(self.y_size)]


def part_1(inp: str) -> int:
    grid = Grid(inp)
    return sum(grid.map(grid.cell_is_visible))


def part_2(inp: str) -> int:
    grid = Grid(inp)
    return max(grid.map(grid.get_scenic_score))


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    with open(f"../../../common/{os.path.split(os.getcwd())[-1]}/input.txt", "r") as fp:
        inp = fp.read()

    part_1_result = part_1(inp)
    print("part 1 result:", part_1_result)

    part_2_result = part_2(inp)
    print("part 2 result:", part_2_result)
