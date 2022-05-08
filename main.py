import argparse
import sys
from hacks import *

parser = argparse.ArgumentParser()
parser.add_argument("-c", nargs='+', help="ciphertext text")
parser.add_argument("-n", nargs='+', help="part (n) of public key")
parser.add_argument("-e", help="exponent")
parser.add_argument("-p", help="p-part")
parser.add_argument("-q", help="q-part")
parser.add_argument('-a', help="name of algorithm: pollard, pq, hastad, dp_brute, wieners, e_phi_not_co_prime")

args = parser.parse_args()

print("Hello!!!")

if args.c and args.n:
    n = args.n
    c = args.c
else:
    print("No arguments, bye")
    sys.exit()

if args.e:
    # e = validation(args.e)
    e = args.e
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
                    m = decryption_crt(e, c, n, p, q)
                    print("Your message: ", m)

            if not flag:
                print("\nHacking by Pollard algorithm\n")
                p, q = pollard_p_1(n)
                if p == -1:
                    print("\nPollard algorithm didn't work\n")
                else:
                    flag = 1
                    m = decryption_crt(e, c, n, p, q)
                    print("\nYour message: ", m)
    else:
        decode_m(hastads_attack(c, n, e))

if args.a == "pollard":
    print("\nHacking by Pollard algorithm\n")
    c = validation(c[0])
    n = validation(n[0])
    p, q = pollard_p_1(n)
    if p == -1:
        print("\nPollard algorithm didn't work\n")
    else:
        flag = 1
        m = decryption(e, c, n, p, q)
        print("\nYour message: ", m)

if args.a == "pq":
    print("\nHacking by P&Q algorithm\n")
    c = validation(c[0])
    n = validation(n[0])
    p, q = is_p_q_close(n)
    if p == -1:
        print("P&Q algorithm didn't work\n")
    else:
        flag = 1
        m = decryption(e, c, n, p, q)
        print("Your message: ", m)

if args.a == "hastad":
    print("\nHacking by Hastad's algorithm\n")
    flag = 1
    print("Your message: ", decode_m(hastads_attack(c, n, e)))

if args.a == "dp_brute":
    print("Just a minute, hacking by bruteforce(by dp)")
    c = validation(c[0])
    n = validation(n[0])
    dp_brute(c, n, e)

if args.a == "wieners":
    print("\nHacking by Wiener's algorithm\n")
    c = validation(c[0])
    n = validation(n[0])
    wieners_attack(e, n, c)

if args.p and args.q and (args.a == "e_phi_not_co_prime"):
    print("\nHacking by e_phi_attack:\n")
    p = args.p
    q = args.q
    e_phi_attack(int(e), int(p), int(q), int(c[0]), int(n[0]))


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
