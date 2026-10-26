from functools import reduce 


numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers, 0)

print(f"Список чисел: {numbers}")
print(f"Сумма чисел: {result}")