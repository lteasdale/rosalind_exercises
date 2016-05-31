#!/usr/bin/env python3

from __future__ import print_function, division, absolute_import
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


def mendel_law1(k, m, n):
    N = k + m + n
    p = (2 * k + m) / (2 * N)
    q = (2 * n + m) / (2 * N)
    prob_dom = p ** 2 + 2 * p * q
    return prob_dom


def mendel_law2(k, m, n):
    N = k + m + n
    p = (k + m) / (N)
    q = (m) / (N)
    p1 = (k + m) / (N)
    q2 = (m) / (N)
    prob_dom = p + (p * q)
    return prob_dom


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    string_file = opts['-t']
    with open(string_file, 'r') as fh:
        k, m, n = map(int, fh.read().strip().split())
    seq2 = mendel_law2(k, m, n)
    print(seq2, file=sys.stderr)
