import os.path

from .main import part_1, part_2


def test_part_1():
    with open(f"../../common/{os.path.split(os.path.split(__file__)[0])[-1]}/sample_input.txt", "r") as fp:
        sample_input = fp.read()

    with open(f"../../common/{os.path.split(os.path.split(__file__)[0])[-1]}/sample_output_1.txt", "r") as fp:
        expected_output = fp.read()

    returned_output = part_1(sample_input)
    assert str(returned_output) == expected_output


def test_part_2():
    with open(f"../../common/{os.path.split(os.path.split(__file__)[0])[-1]}/sample_input.txt", "r") as fp:
        sample_input = fp.read()

    with open(f"../../common/{os.path.split(os.path.split(__file__)[0])[-1]}/sample_output_2.txt", "r") as fp:
        expected_output = fp.read()

    returned_output = part_2(sample_input)
    assert str(returned_output) == expected_output
