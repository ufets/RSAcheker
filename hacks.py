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
    print("Iteration: ")
    while p == 1:
        print("\r", k, end='')
        a = pow(a, k, n)
        p = math.gcd(a - 1, n)
        k += 1
    if p == n:
        return -1, -1
    else:
        q = n // p
        return p, q


def hastads_attack(c, n, e):
    num = c.count()
    table = []
    pr = 1
    for i in num:
        c[i] = validation(c[i])
        table[i][0] = c[i]
        n[i] = validation(n[i])
        pr = pr * n[i]
    for i in num:
        table[i][1] = pr / n[i]
    for i in num:
        table[i][2] = pow(table[i][1], -1, n[i])
    me = 0
    for i in num:
        me = me + table[i][3] * table[i][0] * table[i][1] * table[i][2]
    m = find_n_root(me, e)
    return m
