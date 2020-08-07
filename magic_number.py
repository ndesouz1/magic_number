primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
# números entre (8 - 26) e (44 - 44)
intervalo = list(range(8, 27)) + list(range(49, 50))
is_magic = []
for n in primos:
    quadrado = n ** 2
    if quadrado in intervalo:
        is_magic.append(quadrado)

print(len(is_magic)) # 3