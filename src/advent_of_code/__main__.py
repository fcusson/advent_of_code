"""module to launch years of the advent of code"""

import argparse
import datetime as dt
from argparse import Namespace

from advent_of_code.year2022 import get_result as result_2022

YEARS = {
    2022: result_2022
}


def parse_args() -> Namespace:

    parser = argparse.ArgumentParser(
        "advent of code",
        description="The advent of code challenge utility"
    )

    last_year = dt.datetime.now().year - 1

    parser.add_argument(
        "-y", "--year",
        metavar="YEAR",
        default=last_year,
        type=int,
        help="year number of the advent of code being called",
    )

    parser.add_argument(
        "-r", "--range",
        metavar="RANGE",
        default="",
        nargs='?',
        help=(
            "Range of days to output. Defaults to all. Range is print page "
            "style. Separate values by ';' and '-' means between, inclusively"
        ),
    )

    return parser.parse_args()


def parse_range(day_range: str) -> list[bool]:

    if day_range == "":
        return [True] * 31

    result = [False] * 31

    for entry in day_range.split(';'):

        if '-' in entry:
            start, end = [int(x) for x in entry.split('-')]

            for i in range(start - 1, end):
                result[i] = True

            continue

        result[int(entry) - 1] = True

    return result


def main() -> None:

    config = parse_args()

    date_range = parse_range(config.range)

    YEARS[config.year](date_range)

    input("Press anything to quit...")


if __name__ == '__main__':
    main()
