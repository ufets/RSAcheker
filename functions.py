import math
from binascii import *


def validation(a):
    a = int(a[2:], 16)
    return a


def prime(n):
    local_n = abs(n)
    if local_n % 2 == 0:
        return False
    if local_n < 2:
        return False
    if local_n < 4:
        return True

    root = find_n_root(2, local_n)
    print("root", "=", root)
    for i in range(3, root + 1, 2):
        if i % 1000001 == 0:
            print(i)
        if local_n % i == 0:
            return False
    return True


primes_cash: [None, list[bool]] = None


def prime2(n):
    global primes_cash
    if n < 2:
        return False

    if primes_cash is not None and n < len(primes_cash):
        return primes_cash[n]

    n += 1
    primes = [True] * n
    for base in range(2, int(n ** 0.5 + 1)):
        if primes[base]:
            primes[base*2:n:base] = [False] * (ceil(n / base) - 2)

    primes[0] = primes[1] = False
    primes_cash = primes
    return primes[n - 1]


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


def decryption_crt(e, c, n, p, q):
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    dp = d % (p - 1)
    dq = d % (q - 1)
    q_inv = pow(q, -1, p)
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)
    h = (q_inv * (m1 - m2)) % p
    m = (m2 + h * q) % n

    m = hex(m)
    m = m[2:]
    if len(m) % 2 != 0:
        m = '0' + m
    m = unhexlify(m.replace('L', '')).decode("utf-8", "backslashreplace")
    return m


def continued_fraction(e, n):
    row = []
    # for i in range(i):
    while n % e != 0:
        tmp = e // n
        row.append(tmp)
        n, e = e, n
        n = n - e * tmp
        yield row


def solve_quadratics(a, b, c):
    discr = pow(b, 2) - 4 * a * c
    if discr > 0:
        root = find_n_root(2, discr)
        x1 = (-b + root) // (2 * a)
        x2 = (-b - root) // (2 * a)
        return x1, x2
    elif discr == 0:
        x = -b // (2 * a)
        return x, x
    else:
        return None, None


def req(arr, i, n):
    if i < n - 1:
        up, down = req(arr, i + 1, n)
        new_down = arr[i] * down + up
        return down, new_down
    else:
        return 1, arr[i]
