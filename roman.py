# pylint: disable=C0103
"""Hi"""
import sys
INPUT = sys.argv[1]

PLUS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
MINUS = {"IV": 2, "IX": 2, "XL": 20, "XC": 20, "CD": 200, "CM": 200}
prev_c = ""
total = 0

for c in INPUT:
    total += PLUS.get(c, 0)
    total -= MINUS.get(prev_c + c, 0)
    prev_c = c

print(total)

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         PLUS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         MINUS = {"IV": 2, "IX": 2, "XL": 20, "XC": 20, "CD": 200, "CM": 200}
#         prev_c = ""
#         total = 0

#         for c in s:
#             total += PLUS.get(c, 0)
#             total -= MINUS.get(prev_c + c, 0)
#             prev_c = c

#         return total