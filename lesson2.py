def factor(num):
    factors = [n+1 for n in range(num // 2) if not num % (n+1)]
    factors.append(num)
    return factors


results = factor(24)
print(results)
