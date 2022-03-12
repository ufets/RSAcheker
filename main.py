import math
from binascii import *


def prime(N):
    if N < 2:
        return 0
    for i in range(2, int(math.sqrt(N))):
        if N % i == 0:
            return 1
    return 0


def m_prime(A, B):
    while (A and B):
        if (A > B):
            A = A % B
        else:
            B = B % A
    if (A + B == 1):
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
    while (1):
        if (k * n + 1) % a == 0:
            return (k * n + 1) // a
        else:
            k += 1

def little_exponent_attack(e, c, n, num_of_iterations):
    if e == 3:
        n1 = int(n, 16)
        c1 = int(c, 16)
        k = 0
        while(k < num_of_iterations):
            m = find_cube_root(c1 + k * n1)
            if  m ** 3 % n1 == c1:
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


n = "c7d6bca5802235a56df4faf08d0fb4701e9e94b886a5c3d0c6441c92e3d3a0e6d7549720d814961b53385dc1fbd28237b028a93c10d08b2d47bf31c8bd6f7aa8062c6d7479a2e12734d17d851955de11382cf42137f1fc40839df2562b7a91dc3b6751f6060ceb3090837d760b748997a43a01919a0c8f2c6b1bfb72653de70a8ae197eb1c6780a75914cdacf9aca56af35059b728584e9bb284c4791e8cfed173ec641e7cc5b278ff680086b934c0abb2ec1f431b1d2173eac97019ff5100b0b510fc87ff47a07e7c748f67c768d7dd739adfdd7d082e933d6038ca554f3282d7aa9072028f4353dbef515b8eb6ff5867c039e1bd1f807a0cbed4655862060f"
c = "408cea43c51328421cb65e91129e81415ff8b3dff50495c278d6c803a33469713a477c8ff1541dc2047316360484de5888d2edfc761ddf23669f5de808891773d497e6f00eac4592f2c339e1caa0ba565be95a84359dcd8b9cc19b0224fc0d4b1ce3248137684ac798f1a64702be243cdd6ca3f3aabdf2eaecc1d0f9314abbd5e6b1887038631f403a4ce083473bf1c8708b212038c5656522ee045983ee0adb4a03ef7866e37f297ea849640a477de99aa45685ce9d2a4c1eb8f319184d2ff2518b70251a1baeabf04c69a78f7e1cade887a75c8832ab2ffcf745bf48443f2dd1b19496760e2e2e9ae84becbfc19d7533082723322c6a8c56617e872a6c25d2"


m = little_exponent_attack( 3, c, n, 10000)
if m!=-1:
    m = decode_m(m)
    print(m)

'''
# CRYPTION + DECRYPTIOM

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

