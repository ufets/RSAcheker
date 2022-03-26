import argparse
from hacks import *

parser = argparse.ArgumentParser()
parser.add_argument("--c", help="ciphertext text")
parser.add_argument("--n", help="part (n) of public key")
parser.add_argument("--e", help="exponent")

args = parser.parse_args()

print("Hello!!!")

if args.c and args.n:
    n = validation(args.n)
    c = validation(args.c)

    if args.e:
        e = validation(args.e)
    else:
        e = 3

    flag = 0

    if e != 3:
        if not flag:
            try:
                p, q = pollard_p_1(n)
                flag = 1
            except -1:
                m = -1
                print("Pollard algorithm didn`t work")
            else:
                m = decryption(e, c, n, p, q)

        if not flag:
            try:
                p, q = is_p_q_close(n)
                flag =1
            except -1:
                m = -1
                print("P&Q algorithm didn`t work")
            else:
                m = decryption(e, c, n, p, q)

    else:
        m = little_exponent_attack(3, c, n)
        m = decode_m(m)

    if m != -1:
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
