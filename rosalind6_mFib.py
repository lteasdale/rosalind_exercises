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


def rabbit_counter(month, life_months):
    n_pairs_minus_1 = 1
    n_pairs_minus_2 = 1
    n_pairs_m_lm = [1, 1]
    current = 1
    for i in range(3, month + 1):
        if len(n_pairs_m_lm) == life_months:
            current = n_pairs_minus_1 + n_pairs_minus_2 - n_pairs_m_lm.pop(0)
            n_pairs_m_lm.append(n_pairs_minus_1)
            n_pairs_minus_2 = n_pairs_minus_1
            n_pairs_minus_1 = current
        else:
            current = n_pairs_minus_1 + n_pairs_minus_2
            n_pairs_m_lm.append(n_pairs_minus_1)
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
