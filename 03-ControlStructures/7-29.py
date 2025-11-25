def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


N = int(input("Podaj N: "))

count = 0
num = 2

print("Pierwsze", N, "liczb pierwszych:")

while count < N:
    if is_prime(num):
        print(num)
        count += 1
    num += 1