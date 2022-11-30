# Advent Of Code 2022
<img src="https://img.shields.io/github/workflow/status/issy/Advent-Of-Code-2022/tests?label=tests&style=for-the-badge">
<img src="https://img.shields.io/github/workflow/status/issy/Advent-Of-Code-2022/linting?label=linting&style=for-the-badge">

This is just a little repo to hold my solutions for the Advent Of Code challenge for 2022

To get started, create a python venv (make sure you have at least version 3.10), install the project requirements and run `python3 scripts/new_day.py`

From there, you can fill in your sample input/outputs and your actual problem input in the directory `src/day_X/` where X is the day of the month.

## Testing

This repo is set up with a test pipeline, so pytest will automatically run tests for each day based on sample input/output

You can run this manually with `python3 -m pytest`

## Developing

Include your solutions in `main.py` in the day directory. Feel free to add extra files if you need to provide abstractions for certain solutions. Calling part 1 from part 2 of a challenge is fine, too.

Run your code with `python3 src/day_X/main.py`
