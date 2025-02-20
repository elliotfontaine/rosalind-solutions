"""
Copyright (c) 2025 Elliot Fontaine - MIT License
Rosalind Solutions
Problem 4 : Rabbits and Recurrence Relations
"""

import sys

file = sys.argv[1]
with open(file, encoding="utf-8") as f:
    parameters = f.read().strip().split()
    parameters = list(map(int, parameters))


def fib(n: int, k: int) -> int:
    """Return the number of rabbit pairs after n months with k offspring per pair."""
    if n > 2:
        return fib(n - 1, k) + k * fib(n - 2, k)
    if n in [1, 2]:
        return 1


print(fib(*parameters))
