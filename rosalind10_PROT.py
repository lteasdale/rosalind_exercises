#!/usr/bin/env python3

from __future__ import print_function, division, absolute_import
from os import path

import docopt
import sys
import screed

__author__ = "lteasnail"

CLI_ARGS = """
USAGE:
rosalind10_PROT.py [options]

OPTIONS:
 -t FILE        A fasta file with one RNA sequence.

This script translates RNA to amino acids.
"""

codon_table = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F',
               'CUC': 'L', 'AUC': 'I', 'GUC': 'V', 'UUA': 'L', 'CUA': 'L',
               'AUA': 'I', 'GUA': 'V', 'UUG': 'L', 'CUG': 'L', 'AUG': 'M',
               'GUG': 'V', 'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
               'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'UCA': 'S',
               'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'UCG': 'S', 'CCG': 'P',
               'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 'CAU': 'H', 'AAU': 'N',
               'GAU': 'D', 'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
               'UAA': '*', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'UAG': '*',
               'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'UGU': 'C', 'CGU': 'R',
               'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R', 'AGC': 'S',
               'GGC': 'G', 'UGA': '*', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
               'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
               }

# This function passes through the sequence and yeilds codons


def codon_yielder(filename):
    for seq in screed.open(filename):
        seq = seq.sequence
    for i in range(0, len(seq)-2, 3):
        codon = seq[i:i+3]
        yield codon


def codon_translator(codon):
    return codon_table[codon]


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    fasta_file = opts['-t']
    codon_iter = codon_yielder(fasta_file)
    translated_sequence = []
    for codon in codon_iter:
        aa = codon_translator(codon)
        translated_sequence.append(aa)
    translated_sequence_joined = ''.join(translated_sequence)
    print(translated_sequence_joined, file=sys.stderr)
