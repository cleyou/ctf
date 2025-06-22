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
# resultat = 8430283130287431302827313028313074891228374817286956447676649476
