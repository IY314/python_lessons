def is_factor(num, y):
    if num % y != 0:
        return False
    else:
        return True

def factor(num):
    factors = []
    for y in range(1, int(num/2)+1):
        if is_factor(num, y):
            factors.append(y)
    factors.append(num)
    return factors


results = factor(24)
print(results)
