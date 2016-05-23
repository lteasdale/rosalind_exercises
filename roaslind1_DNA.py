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


def base_counter(stringy):
    base_count = {}
    for base in stringy:
        base_count[base] = base_count.get(base, 0) + 1
    return base_count['A'], base_count['C'], base_count['G'], base_count['T']


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    string_file = opts['-t']
    string_filey = open(string_file, 'r')
    stringy = string_filey.read()
    c1, c2, c3, c4 = base_counter(stringy)
    print('{} {} {} {}'.format(c1, c2, c3, c4), file=sys.stderr)
