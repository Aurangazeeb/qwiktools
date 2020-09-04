#!/usr/bin/env python3
"""Print a pyramid to the terminal

A pyramid of height 3 would look like:

--=--
-===-
=====

"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter


def print_pyramid(rows):
    """Print a pyramid of a given height

    :param int rows: total height
    """
    if(rows > 0):
        max_num_equals = 2 * rows - 1
        hipen_count_list = list(range(max_num_equals - 1, -2, -2))
        equals_count_list = list(range(1, max_num_equals + 2, 2))

        for hiphen_count, equals_count in zip(hipen_count_list, equals_count_list):
                print('-' * (hiphen_count//2), end='')
                print('=' * equals_count, end='')
                print('-' * (hiphen_count//2), end='\n')
    else:
        raise ValueError('Pyramid height should be a positive integer')


if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )

###############################################################
# added type = int
    parser.add_argument("-r", "--rows", default=10, type= int, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(args.rows)
