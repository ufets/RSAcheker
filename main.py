import math
from binascii import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--c", help="encrypted text")
parser.add_argument("--n", help="part (n) of public key")

args = parser.parse_args()


def prime(N):
    if N < 2:
        return 0
    for i in range(2, int(math.sqrt(N))):
        if N % i == 0:
            return 1
    return 0


def m_prime(A, B):
    while A and B:
        if A > B:
            A = A % B
        else:
            B = B % A
    if A + B == 1:
        return 1
    else:
        return 0


def find_cube_root(n):
    lo = 0
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        if mid ** 3 < n:
            lo = mid + 1
        else:
            hi = mid
    return lo


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


print("Hello!!!")
if args.c and args.n:
    n = args.n[2:]
    c = args.c[2:]
    m = little_exponent_attack(3, c, n, 10000)
    if m != -1:
        m = decode_m(m)
        print("\nmessage:", m)
    else:
        print("hmm, something is wrong...")

'''
# CRYPTION + DECRYPTION

#key generation
p = 359334085968622831041960188598043661065388726959079837
q = 35742549198872617291353508656626642567
n = p * q
phi = (p - 1) * (q - 1)

e = 3

#cryption
m = str(input("text your message:"))
m = m.encode("utf-8").hex()
print("hex=",m)
m = int(m, 16)
c = pow(m, e, n)

# decryption
d = pow(e, -1, phi)
m = pow(c, d, n)
m = hex(m)
m = m[2:]
if len(m) %2 != 0:
    m = '0' + m
m = unhexlify(m.replace('L', '')).decode("utf-8", "backslashreplace")

print("message:", m)


'''

'''
from binascii import unhexlify

# string_to_int
# string ---> hex_string(hex_value) ---> int

plaintext = 'hello'
hex_plaintext = plaintext.encode("utf-8").hex()
print(hex_plaintext)
value = int(hex_plaintext, 16)
print(value)

# SHORT VERSION(better use this one)
value2 = int(plaintext.encode("utf-8").hex(), 16)
print(value2)
# now you can operate with value

# int_to_string
string = unhexlify(hex(value)[2:].replace('L', '')).decode()
print(string)
'''
