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


def mod_inv(a, n):
    k = 1
    while (1):
        if (k * n + 1) % a == 0:
            return (k * n + 1) // a
        else:
            k += 1


print("Hello!!!")



p = 337 #int(input("p="))
while (prime(p) != 0):
    p = int(input("please,try again\n"))

q = 997 #int(input("q="))
while (prime(q) != 0):
    q = int(input("please,try again\n"))

n = p * q
phi = (p - 1) * (q - 1)

print("e[1;", phi, "]:")
e = 5#int(input())
while ((e <= 1) or (e >= phi) or (m_prime(e, phi) != 1)):
    e = int(input("please,try again\n"))



#______________________________________

m = str(input("text your message:"))

m = m.encode("utf-8").hex()

print(m)

m = int(m,16)

print(m)

c = pow(m, e, n)
print("c=",c)
# ______________________________________________
# decryption


# pow(-1, e, phi)
d = mod_inv(e, phi)
print("d =", d)

m = pow(c, d)
m = m % n
print("m10=",m)
m = hex(m)

print("m16=",m)

m = '0'+ m[2:]
print(m)

print(unhexlify(m).decode())

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

