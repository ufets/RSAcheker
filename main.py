import argparse
from functions import *

parser = argparse.ArgumentParser()
parser.add_argument("--c", help="ciphertext text")
parser.add_argument("--n", help="part (n) of public key")

args = parser.parse_args()

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
# ENCRYPTION + DECRYPTION

#key generation
p = 359334085968622831041960188598043661065388726959079837
q = 35742549198872617291353508656626642567
n = p * q
phi = (p - 1) * (q - 1)

e = 3

#encryption
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
