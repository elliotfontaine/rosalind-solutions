"""
Copyright (c) 2025 Elliot Fontaine - MIT License
Rosalind Solutions
Problem 1 : Counting DNA Nucleotides
"""

import sys


file = sys.argv[1]
with open(file, encoding="utf-8") as f:
    seq = f.read().strip()

for nuc in "ACGT":
    print(seq.count(nuc), end=" ")
