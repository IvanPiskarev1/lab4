import random


def random_numbers(start, end, count):
    for _ in range(count):
        yield random.randint(start, end)


start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
count = int(input("Введите количество чисел: "))

print("Сгенерированное(ые) число(а): ")

for number in random_numbers(start, end, count):
    print(number, end=" ")