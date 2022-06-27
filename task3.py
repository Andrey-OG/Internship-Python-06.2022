# task3
from math import log, ceil, floor


def zeros(n):
    result = 0
    while n >= 5:
        n //= 5
        result += n
    return result

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
