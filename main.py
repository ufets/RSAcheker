import argparse
import sys
from hacks import *

parser = argparse.ArgumentParser()
parser.add_argument("-c", nargs='+', help="ciphertext text")
parser.add_argument("-n", help="part (n) of public key")
parser.add_argument("-e", help="exponent")
parser.add_argument('-a', help="name of algorithm: pollard, pq")

args = parser.parse_args()

print("Hello!!!")

if args.c and args.n:
    n = validation(args.n)
    '''make c a container'''
    c = args.c
else:
    print("No arguments, bye")
    sys.exit()

if args.e:
    e = validation(args.e)
else:
    e = 3

if args.a is None:
    if len(c) == 1:

        c = validation(c[0])

        if e == 3:
            print("\nHacking by little exponent attack:\n")

            m = little_exponent_attack(3, c, n)
            if m != -1:
                m = decode_m(m)
                print("Your message: ", m)
            else:
                print("Little exponent attack didn't work\n")

        else:

            flag = 0

            if not flag:
                print("\nHacking by P&Q algorithm\n")
                p, q = is_p_q_close(n)
                if p == -1:
                    print("P&Q algorithm didn't work\n")
                else:
                    flag = 1
                    m = decryption(e, c, n, p, q)
                    print("Your message: ", m)

            if not flag:
                print("\nHacking by Pollard algorithm\n")
                p, q = pollard_p_1(n)
                if p == -1:
                    print("\nPollard algorithm didn't work\n")
                else:
                    flag = 1
                    m = decryption(e, c, n, p, q)
                    print("\nYour message: ", m)
    else:
        crt()
else:

    c = validation(c[0])

    if args.a == "pollard":
        print("\nHacking by Pollard algorithm\n")
        p, q = pollard_p_1(n)
        if p == -1:
            print("\nPollard algorithm didn't work\n")
        else:
            flag = 1
            m = decryption(e, c, n, p, q)
            print("\nYour message: ", m)

    if args.a == "pq":
        print("\nHacking by P&Q algorithm\n")
        p, q = is_p_q_close(n)
        if p == -1:
            print("P&Q algorithm didn't work\n")
        else:
            flag = 1
            m = decryption(e, c, n, p, q)
            print("Your message: ", m)


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
