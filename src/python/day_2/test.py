import os.path

from .main import part_1, part_2, calculate_move_from_outcome, calculate_score


def test_part_1():
    with open(f"../../common/{os.path.split(os.path.split(__file__)[0])[-1]}/sample_input.txt", "r") as fp:
        sample_input = fp.read()

    with open(f"../../common/{os.path.split(os.path.split(__file__)[0])[-1]}/sample_output_1.txt", "r") as fp:
        expected_output = fp.read()

    returned_output = part_1(sample_input)
    assert returned_output == int(expected_output)


def test_part_2():
    with open(f"../../common/{os.path.split(os.path.split(__file__)[0])[-1]}/sample_input.txt", "r") as fp:
        sample_input = fp.read()

    with open(f"../../common/{os.path.split(os.path.split(__file__)[0])[-1]}/sample_output_2.txt", "r") as fp:
        expected_output = fp.read()

    returned_output = part_2(sample_input)
    assert returned_output == int(expected_output)


def test_outcome_predictor():
    outcomes = [
        [0, 0, 2],
        [0, 1, 0],
        [0, 2, 1],
        [1, 0, 0],
        [1, 1, 1],
        [1, 2, 2],
        [2, 0, 1],
        [2, 1, 2],
        [2, 2, 0]
    ]
    for enemy_move, desired_outcome, expected_outcome in outcomes:
        assert calculate_move_from_outcome(enemy_move, desired_outcome) == expected_outcome


def test_score_calculator():
    scores = [  # opponent move, my move, my score
        [1, 0, 1],
        [2, 1, 2],
        [0, 2, 3],
        [0, 0, 4],
        [1, 1, 5],
        [2, 2, 6],
        [2, 0, 7],
        [0, 1, 8],
        [1, 2, 9],
    ]
    for enemy_move, my_move, expected_score in scores:
        assert calculate_score(enemy_move, my_move) == expected_score
