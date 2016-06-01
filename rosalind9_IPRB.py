#!/usr/bin/env python3

from __future__ import print_function, division, absolute_import
from os import path

import docopt
import sys

__author__ = "lteasnail"

CLI_ARGS = """
USAGE:
rosalind8_IPRB.py [options]

OPTIONS:
 -t FILE       File containing three numbers, k, m, n. k is the number of
               individuals that are homozygous dominant for a factor, m are
               heterozygous, and nn are homozygous recessive.

This script returns the probability that two randomly selected mating
organisms will produce an individual possessing a dominant allele (and thus
displaying the dominant phenotype). Assuming that any two organisms can mate.
"""

# This functions returns the probablity that an offspring will possess a
# dominant allele if you assume hardy weinberg equilibrium.


def mendel_law_hardyW(k, m, n):
    N = k + m + n
    p = (2 * k + m) / (2 * N)
    q = (2 * n + m) / (2 * N)
    prob_dom = p ** 2 + 2 * p * q
    return prob_dom

# This functions returns the probablity that an offspring will possess a
# dominant allele if the population size is fixed.


def mendel_law_fixed_pop(k, m, n):
    N = k + m + n
    # select dominant first
    dom1 = (k/N)
    # select a heterozygous first
    het1dom2 = (m/N)*(k/(N-1))
    het1het2 = (m/N)*((m-1)/(N-1))*(0.75)
    het1rec2 = (m/N)*(n/(N-1))*(0.5)
    het1 = het1dom2 + het1het2 + het1rec2
    # select recessive first
    rec1dom2 = (n/N)*(k/(N-1))
    rec1het2 = (n/N)*(m/(N-1))*(0.5)
    rec1 = rec1dom2 + rec1het2
    return dom1 + het1 + rec1


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    string_file = opts['-t']
    with open(string_file, 'r') as fh:
        k, m, n = map(int, fh.read().strip().split())
    prob_dom = mendel_law_fixed_pop(k, m, n)
    print(prob_dom, file=sys.stderr)
