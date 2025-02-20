"""
Copyright (c) 2025 Elliot Fontaine - MIT License
Rosalind Solutions
Problem 5 : Computing GC Content
"""

import sys


def parse_fasta(file: str) -> dict:
    """
    Parse a FASTA file and return a dictionary with the definition line as key
    and the sequence as value.
    - Both interleaved and sequential sequence representations are allowed.
    - Comment lines starting with `;` are ignored.
    - Sequence content isn't validated.
    """
    sequences = {}
    defline = None
    line_num = 0
    with open(file, encoding="utf-8") as f:
        for line in f:
            line_num += 1
            line = line.strip()
            if not line or line.startswith(";"):
                continue
            if line.startswith(">"):
                defline = line[1:].strip()
                if defline in sequences:
                    raise ValueError(f"Duplicate sequence ID: {defline}")
                sequences[defline] = ""
            elif defline:
                sequences[defline] += line
            else:
                raise ValueError(f"FASTA format error at line {line_num}: {line}")
        return sequences


seqs = parse_fasta(sys.argv[1])
max_gc = ("ID", 0)
for seq_id, seq in seqs.items():
    gc_content = (seq.count("G") + seq.count("C")) / len(seq) * 100
    if gc_content > max_gc[1]:
        max_gc = (seq_id, gc_content)
print(*max_gc, sep="\n")
