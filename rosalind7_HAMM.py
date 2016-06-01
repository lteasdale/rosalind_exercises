#!/usr/bin/env python3

from __future__ import print_function, division, absolute_import
from os import path

import docopt
import sys
import screed

__author__ = "lteasnail"

CLI_ARGS = """
USAGE:
rosalind7_HAMM.py [options]

OPTIONS:
 -t FILE        A fasta file with two sequences of equal length

This script counts the number of differences between the two sequences.
"""


def HAMM_counter(filename):
    with screed.open(filename) as seqfile:
        counts = 0
        reads = []
        for read in seqfile:
            reads.append(read.sequence)
        seq1, seq2 = reads
        seq_1_split = list(seq1)
        seq_2_split = list(seq2)
        for base in range(len(seq_1_split)):
            if seq_1_split[base] != seq_2_split[base]:
                counts += 1
    return counts


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    fasta_file = opts['-t']
    counts = HAMM_counter(fasta_file)
    print(counts, file=sys.stderr)
