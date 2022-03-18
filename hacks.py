from functions import *


def little_exponent_attack(e, c, n, num_of_iterations=10000):
    if e == 3:
        print("Just a minute, hacking by bruteforce...")
        k = 0
        while k < num_of_iterations:
            m = find_cube_root(c + k * n)
            if m ** 3 % n == c:
                return m
            k += 1
    return -1


def is_p_q_close(n, num_of_iterations=10000):
    t = find_n_root(2, n)
    for i in range(num_of_iterations):
        s2 = (t + i)**2 - n
        if float(s2).is_integer():
            s = find_n_root(2, s2)
            p = t + s
            q = t - s
            return p, q
    return -1, -1