"""
Copyright (c) 2025 Elliot Fontaine - MIT License
Rosalind Solutions
Problem 6 : Counting Point Mutations
"""

import sys


def hamming_distance(seq_1: str, seq_2: str) -> int:
    """
    Return the Hamming distance between two sequences.
    """
    return sum(1 for nucl_a, nucl_b in zip(seq_1, seq_2) if nucl_a != nucl_b)


file = sys.argv[1]
with open(file, encoding="utf-8") as f:
    seq1, seq2 = f.read().strip().splitlines()

print(hamming_distance(seq1, seq2))
