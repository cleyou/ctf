from functools import reduce
from operator import xor
from typing import List

def f(x: List[int]) -> List[int]:
    return list(map(lambda c: c ^ 42, x))

def g(x: List[int]) -> List[int]:
    return list(reversed(x))

def h(x: str) -> List[int]:
    return list(map(lambda c: ord(c) + 1, x))

def encrypt(clair: str) -> List[int]:
    return f(g(h(clair)))

# encryptage
crypte = encrypt(flag)
# resultat = 
# [84, 30, 28, 31, 30, 28, 74, 31, 30, 28, 27, 31, 30, 28, 31, 30, 74, 89, 122, 83, 74, 81, 72, 86, 95, 64, 4, 76, 76, 64, 94, 76]
