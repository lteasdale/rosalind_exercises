#!/usr/bin/env python3

from __future__ import print_function, division, absolute_import
from os import path

import docopt
import sys
import screed

__author__ = "lteasnail"

CLI_ARGS = """
USAGE:
alignment_summerise.py [options]

OPTIONS:
 -t STRING        String to count

counts the number of each base pair
"""


def pattern_finder(filename):
    with screed.open(filename) as seqfile:
        counts = 0
        reads = []
        pattern_starts = []
        for read in seqfile:
            reads.append(read.sequence)
        seq1, pattern = reads
        for i in range(len(seq1)-len(pattern) + 1):
            counts += 1
            if seq1[i:i+len(pattern)] == pattern:
                pattern_starts.append(counts)
    return pattern_starts


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    fasta_file = opts['-t']
    counts = pattern_finder(fasta_file)
    print(*counts, file=sys.stderr)
