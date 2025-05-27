from functools import lru_cache

def is_scramble(s1: str, s2: str) -> bool:
    # Si las longitudes no coinciden, no pueden ser scramble
    if len(s1) != len(s2):
        return False
    # Si son iguales, es claramente válido
    if s1 == s2:
        return True
    # Si los caracteres no coinciden (en cantidad), tampoco puede ser válido
    if sorted(s1) != sorted(s2):
        return False

    @lru_cache(maxsize=None)
    def dfs(a: str, b: str) -> bool:
        if a == b:
            return True
        if sorted(a) != sorted(b):
            return False
        n = len(a)
        for i in range(1, n):
            # Sin swap
            if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                return True
            # Con swap
            if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i]):
                return True
        return False

    return dfs(s1, s2)

# Casos de prueba
print(is_scramble("great", "rgeat"))  # True
print(is_scramble("abcde", "caebd"))  # False
print(is_scramble("a", "a"))          # True
print(is_scramble("abc", "bca"))      # True
print(is_scramble("abc", "cab"))      # True
print(is_scramble("abc", "acb"))      # True
