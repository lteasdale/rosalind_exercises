#!/usr/bin/env python3

from __future__ import print_function
from os import path

import docopt
import sys

__author__ = "lteasnail"

CLI_ARGS = """
USAGE:
alignment_summerise.py [options]

OPTIONS:
 -t STRING        String to count

counts the number of each base pair
"""


def rabbit_counter(month, kids):
    n_pairs_minus_1 = 1
    n_pairs_minus_2 = 1
    current = 1
    for i in range(3, month + 1):
        current = n_pairs_minus_1 + n_pairs_minus_2 * kids
        n_pairs_minus_2 = n_pairs_minus_1
        n_pairs_minus_1 = current
    return current

# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    string_file = opts['-t']
    with open(string_file, 'r') as fh:
        n, k = map(int, fh.read().strip().split())
    seq2 = rabbit_counter(n, k)
    print(seq2, file=sys.stderr)
