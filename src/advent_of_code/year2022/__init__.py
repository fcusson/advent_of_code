"""advent of code 2022"""

from advent_of_code.year2022.day_1 import day_1
from advent_of_code.year2022.day_2 import day_2
from advent_of_code.year2022.day_3 import day_3

SOLUTIONS = [
    day_1,
    day_2,
    day_3,
]


def get_result(days: list[bool] = [True] * 31) -> None:

    for index, solution in enumerate(SOLUTIONS):

        if days[index]:
            print(f"Day {index} -> {solution()}")
