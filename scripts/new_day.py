import sys
import os
from datetime import datetime
import shutil


frameworks = {
    "python": {
        "base_path": "python",
        "files": (
            ("__init__.py", None),
            ("main.py", "main.py.template"),
            ("test.py", "test.py.template")
        )
    },
    "typescript": {
        "base_path": "typescript",
        "files": (
            ("index.ts", "index.ts.template"),
            ("index.ts.spec", "index.spec.ts.template")
        )
    }
}


def main():
    if len(sys.argv) < 1:
        raise RuntimeError("Missing required argument 'framework'")

    framework = sys.argv[1]
    if framework not in frameworks:
        raise RuntimeError(f"Invalid framework {framework!r} - valid frameworks are {list(frameworks)}")

    day_number = int(sys.argv[2]) if len(sys.argv) == 3 else datetime.now().date().day
    base_path = frameworks[framework]["base_path"]
    day_directory = f"./src/{base_path}/day_{day_number}"
    if os.path.exists(day_directory):
        raise RuntimeError(f"Directory for day {day_number} already exists")

    os.mkdir(day_directory)

    if not os.path.exists(f"./common/day_{day_number}"):
        os.mkdir(f"./common/day_{day_number}")
        for filename in ("input.txt", "sample_input.txt", "sample_output_1.txt", "sample_output_2.txt"):
            with open(f"./common/day_{day_number}/{filename}", "w"):
                pass

    for filename, template_name in frameworks[framework]["files"]:
        filepath = f"{day_directory}/{filename}"
        if template_name is None:
            with open(filepath, "w"):
                pass
        else:
            shutil.copyfile(f"./templates/{template_name}", filepath)

    print(f"Initialised {framework} directory for day {day_number}")


if __name__ == "__main__":
    main()
