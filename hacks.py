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
        s = find_n_root(2, s2)
        p = t + s
        q = t - s
        return p, q
    return -1, -1


def pollard_p_1(n):
    a = 2   # base
    k = 2   # factor
    p = 1
    while 1 <= p < n:
        print("Iteration: ", k)
        a = (a**k) % n
        print("a = ", a)
        p = math.gcd(a - 1, n)
        print("p = ", p)
        if p == 1:
            k += 1
        elif p == n:
            return -1
        else:
            q = n/p
            return p, q

