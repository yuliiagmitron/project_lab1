# Програма для обчислення чисел Фібоначчі

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence

# Введення кількості чисел Фібоначчі, які потрібно обчислити
n = int(input("Введіть кількість чисел Фібоначчі, які ви хочете побачити: "))

# Виклик функції і виведення результату
result = fibonacci(n)
print(f"Перші {n} чисел Фібоначчі: {result}")
