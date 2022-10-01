N = int(input("Введите число N: "))

def multiplier(N):
    if N == 1:
        return 1
    else:
        return N * multiplier(N - 1)

list = []
for e in range(1, N + 1):
    list.append(multiplier(e))

print(f"Произведения чисел от 1 до {N}: {list}")
