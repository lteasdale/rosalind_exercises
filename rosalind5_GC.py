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


def GC_caluator(filename):
    GC_dict = {}
    for seq in screed.open(filename):
        seq_name = seq.name
        seq = seq.sequence
        length = len(seq)
        base_count = {}
        for base in seq:
            base_count[base] = base_count.get(base, 0) + 1
        parp = base_count['C'] + base_count['G']
        GC_content = parp/length
        GC_dict[seq_name] = GC_content
    return GC_dict


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    fasta_file = opts['-t']
    GC_diction = GC_caluator(fasta_file)
    max_GC = 0
    max_name = ''
    for key in GC_diction:
        if GC_diction[key] > max_GC:
            max_GC = GC_diction[key]
            max_name = key
    max_GC = GC_diction[max_name] * 100
    print("{} {}".format(max_name, max_GC), file=sys.stderr)
