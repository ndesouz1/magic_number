is_prime = []

for n in range(8, 27):
    cont = 0

    for i in range(1, n+1):
        if n % i == 0:
            cont += 1

    if cont <= 2:
        is_prime.append(n)

for m in range(49, 49):
    cont = 0

    for i in range(1, m+1):
        if m % i == 0:
            cont += 1

    if cont <= 2:
        is_prime.append(m)
print(is_prime)

#números primos: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,53, 59, 61, 67, 71, 73, 79, 83, 89, 97