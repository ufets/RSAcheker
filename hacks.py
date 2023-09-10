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
        s2 = (t + i) ** 2 - n
        s = find_n_root(2, s2)
        p = t + s
        q = t - s
        return p, q
    return -1, -1


def pollard_p_1(n):
    a = 2  # base
    k = 2  # factor
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


def dp_brute(c, n, e, num=1000000):
    m = 5
    p = 1
    for dp in range(num):
        p = math.gcd(pow(m, dp * e, n) - m, n)
        if p != 1:
            break
    if p == 1:
        print(f"\nBruteforce error! No dp from 1 to {num = }")
    else:
        q = n // p
        m = decryption_crt(e, c, n, p, q)
        print("Your message: ", m)


def wieners_attack(e, n, c):
    for row in continued_fraction(e, n):
        if row == [0]:
            continue
        d, k = req(row, 0, len(row))
        phi = (e * d - 1) // k
        p, q = solve_quadratics(1, n - phi + 1, n)
        if p is None:
            continue

        if p*q == n:
            m = decryption_crt(e, c, n, abs(p), abs(q))
            print("Your message: ", m)
            return


def e_phi_attack(e, p, q, c, n, flag):
    r = (p-1)*(q-1) // math.gcd(p-1, q-1)
    d = pow(e, -1, r//e)
    for i in range(e):
        m = decode_m(pow(pow(c, d, n) * pow(pow(2, r//e, n), i, n), 1, n))
        if m.find(flag, 0) != -1:
            print("message:", m, "\n\n")
            break
