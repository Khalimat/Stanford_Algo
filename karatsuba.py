def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y

    max_len = max(len(str(x)),
                  len(str(y)))

    n = round(max_len / 2)

    a = x // (10 ** n)
    b = x % (10 ** n)

    c = y // (10 ** n)
    d = y % (10 ** n)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd
    final_products = (10 ** (2 * n)) * ac + (10 ** n) * ad_bc + bd
    return final_products

