def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def f(n):
    count = 0      # how many primes we have found
    num = 2        # number we are testing

    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1

print(f(5))