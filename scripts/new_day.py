import sys
import os
from datetime import datetime
import shutil


def raise_if_exists(filepath: str):
    if os.path.exists(filepath):
        raise RuntimeError(f"{filepath} already exists")


def touch_file(filepath: str):
    with open(filepath, "w"):
        pass


def main():
    day_number = int(sys.argv[1]) if len(sys.argv) == 2 else datetime.now().date().day
    day_directory = f"./src/day_{day_number}"
    if os.path.exists(day_directory):
        raise RuntimeError(f"Directory for day {day_number} already exists")

    os.mkdir(day_directory)

    for filename, template_name in (
        ("__init__.py", None),
        ("main.py", "main.py.template"),
        ("input.txt", None),
        ("sample_input.txt", None),
        ("sample_output_1.txt", None),
        ("sample_output_2.txt", None),
        ("test.py", "test.py.template"),
    ):
        filepath = f"{day_directory}/{filename}"
        if template_name is None:
            touch_file(filepath)
        else:
            shutil.copyfile(f"./templates/{template_name}", filepath)

    print(f"Initialised day directory for day {day_number}")


if __name__ == "__main__":
    main()
