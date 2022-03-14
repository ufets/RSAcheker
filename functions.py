import math
from binascii import *


def prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(N))):
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


def little_exponent_attack(e, c, n, num_of_iterations):
    if e == 3:
        print("Just a minute, hacking by bruteforce...")
        n1 = int(n, 16)
        c1 = int(c, 16)
        k = 0
        while k < num_of_iterations:
            m = find_cube_root(c1 + k * n1)
            if m ** 3 % n1 == c1:
                return m
            k += 1
    return -1


def decode_m(m):
    m = hex(m)
    m = m[2:]
    if len(m) % 2 != 0:
        m = '0' + m
    m = unhexlify(m.replace('L', '')).decode("utf-8", "backslashreplace")
    return m
