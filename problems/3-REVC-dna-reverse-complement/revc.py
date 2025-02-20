"""
Copyright (c) 2025 Elliot Fontaine - MIT License
Rosalind Solutions
Problem 3 : Complementing a Strand of DNA
"""

import sys


file = sys.argv[1]
with open(file, encoding="utf-8") as f:
    seq = f.read().strip()

translation_table = str.maketrans("ATGC", "TACG")
print(seq.translate(translation_table)[::-1])
