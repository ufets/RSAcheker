import math
from Crypto.Util.number import *

def prime(N):
    if N <2:
        return 0
    for i in range (2, int(math.sqrt(N))):
        if N % i == 0:
            return 1
    return 0


def m_prime(A, B):
    while(A and B):
        if (A > B):
            A = A % B
        else:
            B = B % A
    if (A + B == 1):
        return 1
    else:
        return 0


def mod_inv(a , n):
    k = 1
    while(1):
        if (k * n + 1) % a == 0:
            return (k * n + 1)//a
        else:
            k += 1


print("Hello!")


p = int(input("p="))
while(prime(p) != 0):
    p = int(input("please,try again\n"))


q = int(input("q="))
while(prime(q) != 0):
    q = int(input("please,try again\n"))


n = p * q
phi = (p - 1) * (q - 1)


if (phi > 0):
    print("e[1;",phi,"]:")
    e = int(input())
    while((e <= 1) or (e >= phi) or (m_prime(e , phi) != 1)):
        e = int(input("please,try again\n"))

c = int(input("c ="))

d = mod_inv( e, phi )
print ( "d =", d)

# m = pow(c, d)%n
m =pow(c , d) % n
plaintext = str(long_to_bytes(m,2))[3:-1]
print(plaintext)