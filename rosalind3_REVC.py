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


def DNA_rev_comper(stringy):
    transcribed_sequence = []
    for base in reversed(stringy):
        if base == "T":
            transcribed_sequence.append("A")
        elif base == "A":
            transcribed_sequence.append("T")
        elif base == "C":
            transcribed_sequence.append("G")
        elif base == "G":
            transcribed_sequence.append("C")
    return transcribed_sequence


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    string_file = opts['-t']
    string_filey = open(string_file, 'r')
    stringy = string_filey.read()
    seq2 = DNA_rev_comper(stringy)
    seq3 = ''.join(seq2)
    print(seq3, file=sys.stderr)
