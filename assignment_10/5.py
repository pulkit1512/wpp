def bisection(f, a, b, tol=1e-6):
    while abs(b - a) > tol:
        mid = (a + b) / 2
        if f(mid) == 0:
            return mid
        elif f(mid) * f(a) < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2

f = lambda x: x**3 - x - 2
root = bisection(f, 1, 2)
print(f"Root is approximately {root:.6f}")
