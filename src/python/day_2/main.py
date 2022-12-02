import os


# --- item hierarchy ---

# A/X - rock
# B/Y - paper
# C/Z - scissors

# rock beats scissors
# paper beats rock
# scissors beats paper

# (index + 2) % 3

# --- item scoring ---

# rock - 1
# paper - 2
# scissors - 3

# index % 3 + 1

# --- round scoring ---

# loss - 0
# draw - 3
# win - 6

# I choose rock
# rock = 3
# paper = 0
# scissors = 6

# I choose paper
# rock = 6
# paper = 3
# scissors = 0

# I choose scissors
# rock = 0
# paper = 6
# scissors = 3


def calculate_score(enemy_weapon, my_weapon) -> int:
    won: bool = enemy_weapon == (my_weapon + 2) % 3
    score = my_weapon + 1
    if won:
        score += 6
    elif my_weapon == enemy_weapon:
        score += 3
    return score


def part_1(inp: str) -> int:
    rounds = inp.split("\n")
    total_score = 0
    for a_round in rounds:
        enemy_move, my_move = a_round.split(" ")
        my_weapon: int = "XYZ".index(my_move)
        enemy_weapon: int = "ABC".index(enemy_move)

        total_score += calculate_score(enemy_weapon, my_weapon)

    return total_score


# --- outcomes ---

# rock, win = paper
# rock, draw = rock
# rock, lose = scissors
# XYZ = LDW

# 0 0 = 2
# 0 1 = 0
# 0 2 = 1

# 1 0 = 0
# 1 1 = 1
# 1 2 = 2

# 2 0 = 1
# 2 1 = 2
# 2 2 = 0


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
