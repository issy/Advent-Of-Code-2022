import os.path

import pytest

from .main import part_1, part_2


def get_sample_input_output(input_filename: str, output_filename: str) -> list[tuple[str, int]]:
    base_dir = f"../../common/{os.path.split(os.path.split(__file__)[0])[-1]}"
    with open(f"{base_dir}/{input_filename}", "r") as fp:
        sample_input = fp.read()

    with open(f"{base_dir}/{output_filename}", "r") as fp:
        expected_output = fp.read()

    input_lines = sample_input.splitlines()
    output_lines = expected_output.splitlines()
    return [(input_line, int(output_lines[line_num])) for line_num, input_line in enumerate(input_lines)]


@pytest.mark.parametrize("sample_input,expected_output", get_sample_input_output("sample_input_1.txt", "sample_output_1.txt"))
def test_part_1(sample_input: str, expected_output: int):
    assert part_1(sample_input) == expected_output


@pytest.mark.parametrize("sample_input,expected_output", get_sample_input_output("sample_input_2.txt", "sample_output_2.txt"))
def test_part_2(sample_input: str, expected_output: int):
    assert part_2(sample_input) == expected_output
