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


def crt(c, n):
    table = 0
    # вынос
    num = len(c)
    for i in range(num):
        c[i] = int(c[i])
        n[i] = int(n[i])
    pr = math.prod(n)

    for c_i, n_i in zip(c, n):
        N_i = pr // n_i
        X_i = pow(N_i, -1, n_i)
        table += c_i * N_i * X_i

    return table % pr


def hastads_attack(c, n, e):
    m = crt(c, n)
    m = find_n_root(e, m)
    return m


def dp_brute(c, n, e):
    m = 5
    p = 1
    for dp in range(1000000):
        p = math.gcd(pow(m, dp * e, n) - m, n)
        if p != 1:
            break
    if p == 1:
        print("\nNe poluchilos, ne fartanulo")
    else:
        q = n // p
        m = decryption_crt(e, c, n, p, q)
        print("Your message: ", m)
