"""
Copyright (c) 2025 Elliot Fontaine - MIT License
Rosalind Solutions
Problem 7 : Mendel's First Law
"""

import sys


def dominant_prob(k: int, m: int, n: int) -> float:
    """
    Return the probability that two randomly selected mating organisms will produce
    an offspring with a dominant allele.
    - k: homozygous dominant
    - m: heterozygous
    - n: homozygous recessive
    """

    t = k + m + n
    AAxAA = (k / t) * ((k - 1) / (t - 1))
    AAxAa = (k / t) * (m / (t - 1)) * 2  # symetry, AaxAA
    AAxaa = (k / t) * (n / (t - 1)) * 2  # symetry, aaxAA
    AaxAa = (m / t) * ((m - 1) / (t - 1))
    Aaxaa = (m / t) * (n / (t - 1)) * 2  # symetry, aaxAA
    aaxaa = (n / t) * ((n - 1) / (t - 1))

    # Coefficients can be found using Punnett squares
    dom = 1 * AAxAA + 1 * AAxAa + 1 * AAxaa + 0.75 * AaxAa + 0.5 * Aaxaa + 0 * aaxaa
    return round(dom, 5)


file = sys.argv[1]
with open(file, encoding="utf-8") as f:
    parameters = f.read().strip().split()
    parameters = list(map(int, parameters))
print(dominant_prob(*parameters))
