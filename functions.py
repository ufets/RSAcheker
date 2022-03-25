import math
from binascii import *


def validation(a):
    a = int(a[2:], 16)
    return a


def prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return 1
    return 0


def m_prime(a, b):
    while a and b:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a + b == 1:
        return 1
    else:
        return 0


def find_n_root(root, n):
    low = 0
    high = n
    while low < high:
        middle = (low + high) // 2
        if middle ** root < n:
            low = middle + 1
        else:
            high = middle
    return low


def find_cube_root(n):
    low = 0
    high = n
    while low < high:
        middle = (low + high) // 2
        if middle ** 3 < n:
            low = middle + 1
        else:
            high = middle
    return low


def mod_inv(a, n):
    k = 1
    while 1:
        if (k * n + 1) % a == 0:
            return (k * n + 1) // a
        else:
            k += 1


def decode_m(m):
    m = hex(m)
    m = m[2:]
    if len(m) % 2 != 0:
        m = '0' + m
    m = unhexlify(m.replace('L', '')).decode("utf-8", "backslashreplace")
    return m


def decryption(e, c, n, p, q):
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    m = pow(c, d, n)
    m = hex(m)
    m = m[2:]
    if len(m) % 2 != 0:
        m = '0' + m
    m = unhexlify(m.replace('L', '')).decode("utf-8", "backslashreplace")
    return m

