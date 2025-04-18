"""
This script calculates the factorial of a non-negative integer using a recursive function.

Usage: python factorial.py N

where N is a non-negative integer.

Example: python factorial.py 5
Output: The factorial of 5 is 120.
"""

import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    n = int(sys.argv[1])
    result = factorial(n)
    print(f"The factorial of {n} is {result}.")

