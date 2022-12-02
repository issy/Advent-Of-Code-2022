import os


def calculate_score(enemy_weapon: int, my_weapon: int) -> int:
    weapon_score = my_weapon + 1
    round_score = 3 * (2 - (((enemy_weapon - my_weapon) + 4) % 3))
    return weapon_score + round_score


def part_1(inp: str) -> int:
    rounds = inp.split("\n")
    total_score = 0
    for a_round in rounds:
        enemy_move, my_move = a_round.split(" ")
        my_weapon: int = "XYZ".index(my_move)
        enemy_weapon: int = "ABC".index(enemy_move)

        total_score += calculate_score(enemy_weapon, my_weapon)

    return total_score


def calculate_move_from_outcome(enemy_move: int = 0, desired_outcome: int = 0) -> int:
    return ((enemy_move - 1) + desired_outcome) % 3


def part_2(inp: str) -> int:
    rounds = inp.split("\n")
    total_score = 0
    for a_round in rounds:
        raw_enemy_move, raw_desired_outcome = a_round.split(" ")
        enemy_move = "ABC".index(raw_enemy_move)
        desired_outcome = "XYZ".index(raw_desired_outcome)
        my_move = calculate_move_from_outcome(enemy_move, desired_outcome)
        total_score += calculate_score(enemy_move, my_move)

    return total_score


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    with open(f"../../../common/{os.path.split(os.getcwd())[-1]}/input.txt", "r") as fp:
        inp = fp.read()

    part_1_result = part_1(inp)
    print("part 1 result:", part_1_result)

    part_2_result = part_2(inp)
    print("part 2 result:", part_2_result)
