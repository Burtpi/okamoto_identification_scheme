import math
import random


def number_generator(p, q):
    while True:
        g = random.randrange(1, p-1)
        if pow(g, q, mod=p) == 1:
            return g


def prime_generator():
    flag = True
    while flag:
        flag = False
        x = random.randrange(5, pow(2, 15))
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                flag = True
                break
    return x


def divisor_number(p):
    while True:
        q = prime_generator()
        if q != (p - 1) and (p - 1) % q == 0:
            return q


def parameters_generator():
    p = 23027
    q = 397
    # p = prime_generator()
    # q = divisor_number(p)
    params = {
        "p": p,  # liczba pierwsza p
        "q": q,  # liczba pierwsza q, która jest dzielnikiem (p-1)
        "g1": number_generator(p, q),
        "g2": number_generator(p, q),
        "t": random.randrange(1, 20)
    }
    return params


def key_generator(params: dict):
    secret_key = {
        "a1": random.randrange(0, params["q"]-1),  # losowa liczba z przedziału <0, q>
        "a2": random.randrange(0, params["q"]-1)  # losowa liczba z przedziału <0, q>
    }
    public_key = {
        "g1": params["g1"],
        "g2": params["g2"],
    }
    output = {
        "sk": secret_key,
        "pk": public_key
    }
    return output


def identification(params: dict, keys: dict):
    g1: int = keys["pk"]["g1"]
    g2: int = keys["pk"]["g2"]
    a1: int = keys["sk"]["a1"]
    a2: int = keys["sk"]["a2"]
    p: int = params["p"]
    q: int = params["q"]
    t: int = params["t"]

    k = pow(g1, -a1, mod=p) * pow(g2, -a2, mod=p) % p
    x1 = random.randrange(1, params["q"])
    x2 = random.randrange(1, params["q"])

    u = pow(g1, x1) * pow(g2, x2) % p
    c = random.randrange(0, 2 ** t - 1)

    s1 = x1 + c * a1 % q
    s2 = x2 + c * a2 % q
    v = pow(g1, s1) * pow(g2, s2) * pow(k, c) % p

    if v == u:
        print(f"p: {p} \nq: {q} \ng1: {g1} \ng2: {g2} \na1: {a1} \n"
              f"a2: {a2} \nt: {t} \nk: {k} \nx1: {x1} \nx2: {x2} \n"
              f"u: {u} \nc: {c} \ns1: {s1} \ns2: {s2} \nv: {v}")
        print("Accepted")
    else:
        print("Rejected")


if __name__ == "__main__":
    parameters = parameters_generator()
    keys = key_generator(parameters)
    identification(parameters, keys)
