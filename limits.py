def limit(f, a):
    for h in [0.1, 0.01, 0.001, 0.0001]:
        x = a - h
        print(x, f(x))
    return round(f(a - 0.000001), 3)


def g(x):
    return (x**2 - 1) / (x - 1)


print(limit(g, 1))
