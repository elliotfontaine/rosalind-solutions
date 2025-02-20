"""
Copyright (c) 2025 Elliot Fontaine - MIT License
Rosalind Solutions
Problem 2 : Transcribing DNA into RNA
"""

import sys


file = sys.argv[1]
with open(file, encoding="utf-8") as f:
    seq = f.read().strip()

print(seq.replace("T", "U"))
