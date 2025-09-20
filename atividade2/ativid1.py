count = 0
for i in range(5):
    valor = int(input())
    if valor % 2 == 0:
        count += 1
print(f"{count} valores pares")