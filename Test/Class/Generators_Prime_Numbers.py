def is_prime(n):

    if n < 2:
        return False
    elif n in (2, 3):
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    root = int(n**0.5)+1

    for f in range(5, root, 6):
        if n % f == 0 or n % (f+2) == 0:
            return False

    return True


def prime_gen():

    yield 2
    n = 3
    while True:
        if is_prime(n):
            yield n
        n += 2


p = prime_gen()
print(next(p))
print(next(p))
print(next(p))
print(next(p))

