def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


count = int(input("Введите количество чисел: "))
print("Числа Фибоначчи: ")

for number in fibonacci(count):
    print(number, end=" ")
