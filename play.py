# pylint: disable=C0103
"""Hello DOCSTRING"""
import random

def flip_coin():
    """Simulate a coin flip."""
    return random.choice(["heads", "tails"])

total_heads = 0
total_tails = 0
nbr_of_tries = 100_000_000

for i in range(1, nbr_of_tries + 1):
    if flip_coin() == 'heads':
        total_heads += 1
    else:
        total_tails += 1

print(f"Heads: {total_heads:,}")
print(f"Tails: {total_tails:,}")

print(f"% = {round(total_heads / nbr_of_tries * 100, 2)}")
