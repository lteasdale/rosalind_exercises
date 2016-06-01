#!/usr/bin/env python3

from __future__ import print_function, division, absolute_import
from os import path
import itertools

import docopt
import sys

__author__ = "lteasnail"

CLI_ARGS = """
USAGE:
rosalind11_PERM.py [options]

OPTIONS:
 -t FILE       An interger

This script works out the number of permutations of the integers upto and
including the number in the file. It also prints out the permutations.
"""

# This functions returns the probablity that an offspring will possess a
# dominant allele if you assume hardy weinberg equilibrium.


def permutations(num):
    num = int(num[0])
    nums = ''.join(list(map(str, range(1, num + 1))))
    l = itertools.permutations(str(nums))
    perms = [' '.join(x) for x in l]
    return perms


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    string_file = opts['-t']
    with open(string_file, 'r') as fh:
        num = map(int, fh.read().strip().split())
        perms = permutations(num)
        num_perms = len(perms)
    print(num_perms, file=sys.stdout)
    for perm in perms:
        print(perm, file=sys.stdout)
