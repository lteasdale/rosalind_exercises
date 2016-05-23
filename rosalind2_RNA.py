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


def RNA_transcriber(stringy):
    transcribed_sequence = []
    for base in stringy:
        if base == "T":
            transcribed_sequence.append("U")
        else:
            transcribed_sequence.append(base)
    return transcribed_sequence


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    string_file = opts['-t']
    string_filey = open(string_file, 'r')
    stringy = string_filey.read()
    seq2 = RNA_transcriber(stringy)
    seq3 = ''.join(seq2)
    print(seq3, file=sys.stderr)
